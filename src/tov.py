# from numpy import ndarray
# from scipy.constants import pi
# from scipy.integrate import solve_ivp

# from eos.dimensionless import p_prime


# def tov_rhs(r: float, state: tuple[float, float]) -> tuple[float, float]:
#     # EVERYTHING in this function should be dimensionless
#     p_p, m_p = state
#     # if m <= 0:
#     #     raise ValueError("Initial mass is too small")
#     eps_p = ...
#     f1 = -((m_p * eps_p) / r**2)
#     f2 = 1 + (p_p / eps_p)
#     f3 = 1 + (4 * pi * r**3 * p_p / m_p)
#     f4 = 1 / (1 - (2 * m_p / r))
#     dp_dr = f1 * f2 * f3 * f4
#     dm_dr = (4 * pi) * r**2 * eps_p
#     return (dp_dr, dm_dr)


# def surface_event(r: float, state: tuple[float, float]) -> float:
#     p, _ = state
#     return p


# surface_event.terminal = True  # pyright: ignore[reportFunctionMemberAccess]
# surface_event.direction = -1  # pyright: ignore[reportFunctionMemberAccess]


# def solve_tov(p_c: float) -> tuple[float, float]:
#     p_c_p = p_prime(p_c)
#     eps_p = ...
#     r_0_p = 1e-5
#     m_0_p = (4 * pi / 3) * r_0_p**3 * eps_p
#     solutions = solve_ivp(
#         tov_rhs,
#         t_span=(
#             r_0_p,
#             100,
#         ),  # solve_ivp() should terminate before reaching the endpoint.
#         y0=(p_c_p, m_0_p),
#         events=surface_event,
#         rtol=1e-6,
#         atol=1e-8,
#         max_step=0.1,
#     )
#     radius_surface_events: ndarray = solutions.t_events[0]
#     p_m_surface_events: list[tuple[float, float]] = solutions.y_events[0]
#     if radius_surface_events.size == 0:
#         raise ValueError("No events registered")
#     radius = radius_surface_events[0]
#     mass = p_m_surface_events[0][1]
#     return (radius, mass)


# def generate_mr_curve(
#     p_c_range: list[float],
# ) -> tuple[list[float], list[float]]:
#     radii: list[float] = []
#     masses: list[float] = []
#     for p_c in p_c_range:
#         radius, mass = solve_tov(p_c)
#         radii.append(radius)
#         masses.append(mass)
#     radii = r_nu(radii)
#     masses = m_nu(masses)
#     return (radii, masses)
