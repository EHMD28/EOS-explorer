"""
Polytropic EoS
"""

import numpy as np


@np.vectorize
def eos_p(eps: float, kappa: float, gamma: float) -> float:
    """
    Calculates the pressure [MeV/fm^3] as a function of energy density
    [MeV/fm^3] using a polytropic equation of state.
    """
    return kappa * eps**gamma


@np.vectorize
def eos_eps(p: float, kappa: float, gamma: float) -> float:
    """
    Calculates the energy density [MeV/fm^3] as a function of pressure
    [MeV/fm^3] using a polytropic equation of state.
    """
    # pressure should never be negative, but this is a safeguard anyways
    # if p <= 0:
    #     return 0.0
    return (p / kappa) ** (1 / gamma)
