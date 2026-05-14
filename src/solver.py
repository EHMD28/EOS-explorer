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


EOS_EPS_FN_TYPE = Callable[[float], float]


class TovSolutions:
    """
    Convenient type alias for the object returned from `solve_ivp`, taken directly from
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html
    """

    t: list[float]
    y: list[list[float]]
    t_events: list[list[float]]
    y_events: list[list[tuple[float, float]]]
    status: int


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
    Event for detecting when pressure reaches 0.
    """
    p, _ = state
    return p


surface_event.terminal = True  # pyright: ignore[reportFunctionMemberAccess]
surface_event.direction = -1  # pyright: ignore[reportFunctionMemberAccess]


def get_mr_from_solutions(solutions: TovSolutions) -> tuple[float, float]:
    r_surface_p = None
    m_surface_p = None
    # If a termination event occurs, use the event value. Otherwise, fallback to
    # last values for radius and mass (since both increase monotonically).
    if solutions.status == 1:
        # t_events[0] is a list of surface event radii. t_events[0][0] is the
        # first (and only) radius in that list
        r_surface_p = solutions.t_events[0][0]
        # y_events[0] is a list of surface event states. y_events[0][0] is the
        # first surface event state (a tuple of the form (pressure, mass)).
        m_surface_p = solutions.y_events[0][0][1]
    else:
        # Use the last value of radius solve_ivp found.
        r_surface_p = solutions.t[-1]
        # Use the last value of mass solve_ivp found.
        m_surface_p = solutions.y[1][-1]
    return (r_surface_p, m_surface_p)


def convert_mr_dimensionless_to_physical(r_p: float, m_p: float):
    eps0_SI = ScalingConstants.EPS_0 * ScalingConstants.MEV_FM3_TO_J_M3
    a = c**2 / np.sqrt(G * eps0_SI)
    b = c**4 / np.sqrt(G**3 * eps0_SI)
    r_km = (a * r_p) / 1000  # meters -> kilometers
    m_sol = (b * m_p) / ScalingConstants.M_SUN_IN_KG  # kilograms -> solar mass
    return (r_km, m_sol)


def solve_dimensionless_tov(
    p_c_phys: float, eos_eps_nu_fn: EOS_EPS_FN_TYPE
) -> tuple[float, float]:
    """
    Solve the TOV equation for a given central pressure (`p_c`). The `eos_eps_fn`
    is a callback function which takes in pressure in physical units [MeV/fm^3]
    and outputs energy density in natural units [MeV/fm^3]. Returns a tuple of
    the form (radius_km, mass_msol). See `math/Units.md` for more information
    about internals.
    """

    def eos_eps_prime(p_p: float):
        p_phys = ScalingConstants.EPS_0 * p_p
        eps_phys = eos_eps_nu_fn(p_phys)
        return eps_phys / ScalingConstants.EPS_0

    p_c_p = p_c_phys / ScalingConstants.EPS_0
    eps_c_p = eos_eps_prime(p_c_p)
    # Small initial radius/mass
    r0_p = 1e-5
    m0_p = (4 * pi / 3) * r0_p**3 * eps_c_p
    solutions: TovSolutions = solve_ivp(
        fun=dimensionless_tov_rhs,
        t_span=(r0_p, 100),
        y0=(p_c_p, m0_p),
        args=(eos_eps_prime,),
        events=surface_event,
        max_step=0.01,
        rtol=1e-6,
        atol=1e-8,
    )
    r_surface_p, m_surface_p = get_mr_from_solutions(solutions)
    # Convert scaling constant to SI units so it matches G.
    return convert_mr_dimensionless_to_physical(r_surface_p, m_surface_p)


def generate_mass_radius_curve(
    p_c_exponent_range: tuple[float, float],
    eos_eps_fn: EOS_EPS_FN_TYPE,
) -> tuple[list[float], list[float]]:
    """
    Solve the TOV equation over a range of central pressures. The solver will be
    run for 100 logarithmically spaced points on the interval 10^`p_start` ->
    10^`p_end` (where `p_c_exponent_range` = (`p_start`, `p_end`)) The `eos_eps_fn`
    is a callback function which takes in pressure in natural units [MeV/fm^3]
    and outputs energy density in natural units [MeV/fm^3].
    """
    p_start, p_end = p_c_exponent_range
    p_c_values = np.logspace(p_start, p_end, num=100)
    radii = []
    masses = []
    for p_c in p_c_values:
        radius_km, mass_sol = solve_dimensionless_tov(p_c, eos_eps_fn)
        radii.append(radius_km)
        masses.append(mass_sol)
    # Only include values for which mass increases with respect to the radius.
    df = pd.DataFrame({"p_c": p_c_values, "r": radii, "m": masses})
    max_mass_idx = df["m"].idxmax()
    df = df[:max_mass_idx]
    radii = df["r"].tolist()
    masses = df["m"].tolist()
    return (radii, masses)
