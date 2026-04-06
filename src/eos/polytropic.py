"""
Polytropic EOS
"""

import numpy as np


@np.vectorize
def eos_p(eps: float, kappa: float, gamma: float) -> float:
    """
    Calculates the pressure [MeV/fm^3] as a function of energy density
    [MeV/fm^3] using a polytropic equation of state.
    """
    return kappa * eps**gamma


# def eos_p_vec(densities: list[float], kappa: float, gamma: float) -> list[float]:
#     """
#     Wrapper around `eos_p()` for applying EOS to a range of energy densities.
#     """
#     return [eos_p(eps, kappa, gamma) for eps in densities]


@np.vectorize
def eos_eps(p: float, kappa: float, gamma: float) -> float:
    """
    Calculates the energy density [MeV/fm^3] as a function of pressure
    [MeV/fm^3] using a polytropic equation of state.
    """
    return (p / kappa) ** (1 / gamma)


# def eos_eps_vec(pressures: list[float], kappa: float, gamma: float) -> list[float]:
#     """
#     Wrapper around `eos_eps()` for applying EOS to a range of pressures.
#     """
#     return [eos_eps(p, kappa, gamma) for p in pressures]
