from scipy.constants import pi
from scipy.integrate import solve_ivp


def eos_epsilon(p_prime: float) -> float:
    return 0.0


def tov_rhs(r, state):
    p, m = state
    if m <= 0:
        raise ValueError("r0 is too small")
    if p <= 0:
        return (0, m)
    epsilon = eos_epsilon(p)
    f1 = -((m * epsilon) / r**2)
    f2 = 1 + (p / epsilon)
    f3 = 1 + (4 * pi * r**3 * p / m)
    f4 = 1 / (1 - (2 * m / r))
    dp_dr = f1 * f2 * f3 * f4
    dm_dr = (4 * pi) * r**2 * epsilon
    return (dp_dr, dm_dr)


def surface_event(r, state):
    p, _ = state
    return p


surface_event.terminal = True  # type: ignore
surface_event.direction = -1  # type: ignore


def solve_tov(p_c) -> tuple[float, float]:
    r_0 = 1e-5
    epsilon = eos_epsilon(p_c)
    m_0 = (4 * pi / 3) * r_0**3 * epsilon
    solutions = solve_ivp(
        tov_rhs,
        t_span=(r_0, 50),  # Should terminate before reaching endpoint.
        y0=(p_c, m_0),
        events=surface_event,
    )
    r_surface = solutions.t_events[0][0]
    m_surface = solutions.y_events[0][0][1]
    return (r_surface, m_surface)
