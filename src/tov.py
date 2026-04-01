from numpy import float64, ndarray
from scipy.constants import pi
from scipy.integrate import solve_ivp

from eos import eos_eps_prime, p_prime


def tov_rhs(r: float, state: tuple[float, float]) -> tuple[float, float]:
    # EVERYTHING in this function should be dimensionless
    p, m = state
    if m <= 0:
        raise ValueError("Mass is too small")
    eps = eos_eps_prime(p)
    f1 = -((m * eps) / r**2)
    f2 = 1 + (p / eps)
    f3 = 1 + (4 * pi * r**3 * p / m)
    f4 = 1 / (1 - (2 * m / r))
    dp_dr = f1 * f2 * f3 * f4
    dm_dr = (4 * pi) * r**2 * eps
    return (dp_dr, dm_dr)


def surface_event(r: float, state: tuple[float, float]) -> float:
    p, _ = state
    return p


surface_event.terminal = True  # pyright: ignore[reportFunctionMemberAccess]
surface_event.direction = -1  # pyright: ignore[reportFunctionMemberAccess]


def solve_tov(p_c: float) -> tuple[float, float]:
    p_c_prime = p_prime(p_c)
    eps = eos_eps_prime(p_c_prime)
    r_0 = 1e-2
    m_0 = (4 * pi / 3) * r_0**3 * eps
    solutions = solve_ivp(
        tov_rhs,
        t_span=(r_0, 100),  # solve_ivp() should terminate before reaching the endpoint.
        y0=(p_c, m_0),
        events=surface_event,
    )
    radius_surface_events: ndarray = solutions.t_events[0]
    p_m_surface_events: list[tuple[float, float]] = solutions.y_events[0]
    if radius_surface_events.size == 0:
        raise ValueError("No events registered")
    radius = radius_surface_events[0]
    mass = p_m_surface_events[0][1]
    return (radius, mass)


def generate_mr_curve(
    p_c_range: list[float],
) -> tuple[list[float], list[float]]:
    radii: list[float] = []
    masses: list[float] = []
    for p_c in p_c_range:
        radius, mass = solve_tov(p_c)
        radii.append(radius)
        masses.append(mass)
    return (radii, masses)
