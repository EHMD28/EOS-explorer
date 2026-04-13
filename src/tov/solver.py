"""
Tolman-Oppenheimer-Volkoff equation solver. Note that any time a variable is
suffixed with `_p` (meaning prime), that means that quantity is dimensionless.
"""

from typing import Callable

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.constants import G, c, pi

from app_constants import ScalingConstants


# TODO: Add docstrings
class TOV_Solutions:
    central_pressure: float
    total_radius: float
    total_mass: float
    solver_df: pd.DataFrame

    def __init__(self, solutions, p_c: float):
        ...
        # radius_surface_events: np.ndarray = solutions.t_events[0]
        # state_surface_events: list[tuple[float, float]] = solutions.y_events[0]
        # r_surface_p = None
        # m_surface_p = None
        # # If no events registered (pressure approached 0 asymptotically), then
        # # default to the last values for radii and mass (both of which increase
        # # monotonically).
        # if radius_surface_events.size == 0:
        #     r_surface_p = solutions.t[-1]
        #     m_surface_p = solutions.y[1][-1]
        # else:
        #     r_surface_p = radius_surface_events[0]
        #     p_surface_p, m_surface_p = state_surface_events[0]
        # r_nu = radius_nu(r_surface_p)
        # m_nu = mass_nu(m_surface_p)
        # self.central_pressure = p_c
        # self.total_radius = r_nu
        # self.total_mass = m_nu
        # # Used for displaying the internal values the solver found.
        # self.solver_df = pd.DataFrame(
        #     {
        #         "p_prime": solutions.y[0],
        #         "m_prime": solutions.y[1],
        #         "r_prime": solutions.t,
        #     }
        # )


EOS_EPS_FN_TYPE = Callable[[float], float]


def dimensionless_tov_rhs(
    r_p: float, state: tuple[float, float], eos_eps_p_fn: EOS_EPS_FN_TYPE
):
    """
    Right-hand side of the dimensionless TOV equation. The `eos_eps_p_fn` is a
    callback function which takes dimensionless pressure as input and outputs
    dimensionless energy density.
    """
    p_p, m_p = state
    eps_p = eos_eps_p_fn(p_p)
    # dP/dr split into factors
    f1 = -((m_p * eps_p) / r_p**2)
    f2 = 1 + (p_p / eps_p)
    f3 = 1 + (4 * pi * r_p**3 * p_p / m_p)
    f4 = 1 / (1 - (2 * m_p / r_p))
    dp_dr = f1 * f2 * f3 * f4
    # dm/dr
    dm_dr = (4 * pi) * r_p**2 * eps_p
    return (dp_dr, dm_dr)


def surface_event(r, state: tuple[float, float], eos_eps_p_fn):
    """
    Event for detecting when pressure reaches 0. solve_ivp() detects a zero by
    looking for a sign change. When the pressure is near 0, but small, this
    function forces a sign change.
    """
    p, _ = state
    # # Force pressure to cross 0, triggering the event.
    # altered_p = p - 1e-5
    return p


surface_event.terminal = True  # pyright: ignore[reportFunctionMemberAccess]
surface_event.direction = -1  # pyright: ignore[reportFunctionMemberAccess]


def solve_dimensionless_tov(
    p_c_phys: float, eos_eps_nu_fn: EOS_EPS_FN_TYPE
) -> tuple[float, float]:
    """
    Solve the TOV equation for a given central pressure (`p_c`). The `eos_eps_fn`
    is a callback function which takes in pressure in physical units [MeV/fm^3]
    and outputs energy density in natural units [MeV/fm^3]. Returns a
    `TOV_Solutions` object. See `math/Units.md` for more information about
    internals.
    """

    eps0 = p_c_phys

    def eos_eps_prime(p_p: float):
        p_phys = eps0 * p_p
        eps_phys = eos_eps_nu_fn(p_phys)
        return eps_phys / eps0

    # Since the scaling constant is the central pressure, the dimensionless
    # central pressue is 1.
    p_c_p = 1.0
    eps_c_p = eos_eps_prime(p_c_p)
    # Small initial radius/mass
    r0_p = 1e-5
    m0_p = (4 * pi / 3) * r0_p**3 * eps_c_p
    solutions = solve_ivp(
        fun=dimensionless_tov_rhs,
        t_span=(r0_p, 100),
        y0=(p_c_p, m0_p),
        args=(eos_eps_prime,),
        events=surface_event,
        max_step=0.1,
    )
    r_surface_p = None
    m_surface_p = None
    # Termination Event Occured
    if solutions.status == 1:
        r_surface_p = solutions.t_events[0][0]
        m_surface_p = solutions.y_events[0][0][1]
    else:
        r_surface_p = solutions.t[-1]
        m_surface_p = solutions.y[1][-1]

    # Convert scaling constant to SI units so it matches G.
    eps0_SI = eps0 * ScalingConstants.MEV_FM3_TO_J_M3
    a = c**2 / np.sqrt(G * eps0_SI)
    b = c**4 / np.sqrt(G**3 * eps0_SI)
    r_km = (a * r_surface_p) / 1000
    m_msun = (b * m_surface_p) / ScalingConstants.M_SUN_IN_KG
    return (r_km, m_msun)


def generate_mass_radius_curve(
    p_c_magnitude_range: tuple[float, float],
    eos_eps_fn: EOS_EPS_FN_TYPE,
) -> tuple[list[float], list[float]]:
    """
    Solve the TOV equation over a range of central pressures. The solver will be
    run for 100 logarithmically spaced points on the interval 10^`p_start` ->
    10^`p_end` (where `p_c_magnitude_range` = (`p_start`, `p_end`)) The `eos_eps_fn`
    is a callback function which takes in pressure in natural units [MeV/fm^3]
    and outputs energy density in natural units [MeV/fm^3].
    """
    p_start, p_end = p_c_magnitude_range
    p_c_values = np.logspace(p_start, p_end, num=100)
    radii = []
    masses = []
    for p_c in p_c_values:
        radius_km, mass_msun = solve_dimensionless_tov(p_c, eos_eps_fn)
        radii.append(radius_km)
        masses.append(mass_msun)
    return (radii, masses)
