"""
Tolman-Oppenheimer-Volkoff equation solver. Note that any time a variable is
suffixed with `_p` (meaning prime), that means that quantity is dimensionless.
"""

from typing import Callable

import numpy as np
from scipy.constants import pi
from scipy.integrate import solve_ivp

from dimensionless import (
    energy_density_prime,
    mass_nu,
    pressure_nu,
    pressure_prime,
    radius_nu,
)

EOS_EPS_FN_TYPE = Callable[[float], float]


def dimensionless_tov_rhs(r, state, eos_eps_p_fn):
    """
    Right-hand side of the dimensionless TOV equation. The `eos_eps_p_fn` is a
    callback function which takes dimensionless pressure as input and outputs
    dimensionless energy density.
    """
    p_p, m_p = state
    eps_p = eos_eps_p_fn(p_p)
    # dP/dr split into factors
    f1 = -((m_p * eps_p) / r**2)
    f2 = 1 + (p_p / eps_p)
    f3 = 1 + (4 * pi * r**3 * p_p / m_p)
    f4 = 1 / (1 - (2 * m_p / r))
    dp_dr = f1 * f2 * f3 * f4
    # dm/dr
    dm_dr = (4 * pi) * r**2 * eps_p
    return (dp_dr, dm_dr)


def surface_event(r, state: tuple[float, float], eos_eps_p_fn):
    """
    Event for detecting when pressure reaches 0. solve_ivp() detects a zero by
    looking for a sign change. When the pressure is near 0, but small, this
    function forces a sign change.
    """
    p, _ = state
    # Force pressure to cross 0, triggering the event.
    altered_p = p - 1e-5
    return altered_p


surface_event.terminal = True  # pyright: ignore[reportFunctionMemberAccess]
surface_event.direction = -1  # pyright: ignore[reportFunctionMemberAccess]


def solve_dimensionless_tov(
    p_c: float, eos_eps_fn: EOS_EPS_FN_TYPE
) -> tuple[float, float]:
    """
    Solve the TOV equation for a given central pressure (`p_c`). The `eos_eps_fn`
    is a callback function which takes in pressure in natural units [MeV/fm^3]
    and outputs energy density in natural units [MeV/fm^3]. Returns a tuple
    of the form (radius, mass) where both quantities are in natural units.
    """

    def eos_eps_prime(p_p: float) -> float:
        p_nu = pressure_nu(p_p)
        eps_nu = eos_eps_fn(p_nu)
        return energy_density_prime(eps_nu)

    p_c_p = pressure_prime(p_c)
    eps_p = eos_eps_prime(p_c_p)
    r_0_p = 1e-2
    m_0_p = (4 * pi / 3) * r_0_p**3 * eps_p
    solutions = solve_ivp(
        fun=dimensionless_tov_rhs,
        # solve_ivp() should terminate before reaching the end of the input
        # range.
        t_span=(r_0_p, 100),  # TODO: Tune range
        y0=(p_c_p, m_0_p),
        events=surface_event,
        args=(eos_eps_prime,),
        max_step=0.1,
    )
    radius_surface_events: np.ndarray = solutions.t_events[0]
    state_surface_events: list[tuple[float, float]] = solutions.y_events[0]
    if radius_surface_events.size == 0:
        raise ValueError("No events registered")
    r_surface_p = radius_surface_events[0]
    p_surface_p, m_surface_p = state_surface_events[0]
    r_nu = radius_nu(r_surface_p)
    m_nu = mass_nu(m_surface_p)
    return (r_nu, m_nu)


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
        try:
            radius, mass = solve_dimensionless_tov(p_c, eos_eps_fn)
            radii.append(radius)
            masses.append(mass)
        except ValueError as err:
            print(f"DEBUG - Encountered error: {err}")
    return (radii, masses)
