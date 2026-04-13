"""
Polytropic EoS
"""

import typing

import numpy as np
import pandas as pd


@typing.overload
def eos_p(eps: float, kappa: float, gamma: float) -> float: ...


@typing.overload
def eos_p(eps: list[float], kappa: float, gamma: float) -> list[float]: ...


def eos_p(
    eps: float | list[float], kappa: float, gamma: float
) -> float | list[float] | None:
    """
    Calculates the pressure [MeV/fm^3] as a function of energy density
    [MeV/fm^3] using a polytropic equation of state.
    """
    if isinstance(eps, (float, int)):
        return kappa * eps**gamma
    elif isinstance(eps, (list, np.ndarray, pd.Series)):
        return [kappa * eps_i**gamma for eps_i in eps]


@typing.overload
def eos_eps(p: float, kappa: float, gamma: float) -> float: ...


@typing.overload
def eos_eps(p: list[float], kappa: float, gamma: float) -> list[float]: ...


def eos_eps(
    p: float | list[float], kappa: float, gamma: float
) -> float | list[float] | None:
    """
    Calculates the energy density [MeV/fm^3] as a function of pressure
    [MeV/fm^3] using a polytropic equation of state.
    """
    if isinstance(p, (float, int)):
        return (p / kappa) ** (1 / gamma)
    elif isinstance(p, (list, np.ndarray, pd.Series)):
        return [(p_i / kappa) ** (1 / gamma) for p_i in p]
