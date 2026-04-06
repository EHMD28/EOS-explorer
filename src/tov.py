from typing import Callable

from numpy import ndarray, pi
from scipy.integrate import solve_ivp

from eos.dimensionless import eps_prime, p_prime


def dimensionless_tov_rhs(r, state, eos_eps_p_fn):
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


def surface_event(r, state):
    p, _ = state
    return p


surface_event.terminal = True  # pyright: ignore[reportFunctionMemberAccess]
surface_event.direction = -1  # pyright: ignore[reportFunctionMemberAccess]


def solve_dimensionless_tov(p_c: float, eos_eps_fn: Callable[[float], float]):
    def eos_eps_prime(p: float) -> float:
        # TODO: Check dimensionality of this.
        return eps_prime(eos_eps_fn(p))

    p_c_p = p_prime(p_c)
    # TODO: Fill this in with correct value.
    eps_p = eos_eps_prime(0.0)
    r_0_p = 1e-5
    m_0_p = (4 * pi / 3) * r_0_p**3 * eps_p
    solutions = solve_ivp(
        fun=dimensionless_tov_rhs,
        t_span=(0, 50),  # TODO: Check this
        y0=(p_c_p, m_0_p),
        events=surface_event,
        args=(eos_eps_prime,),
    )
    radius_surface_events: ndarray = solutions.t_events[0]
    p_m_surface_events: list[tuple[float, float]] = solutions.y_events[0]
    if radius_surface_events.size == 0:
        raise ValueError("No events registered")
    radius = radius_surface_events[0]
    mass = p_m_surface_events[0][1]
    return (radius, mass)
