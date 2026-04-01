from pathlib import Path
import numpy as np
import pandas as pd

from app_constants import E_0, EOS_DATA


@np.vectorize
def p_prime(p: float) -> float:
    return p / E_0


@np.vectorize
def eps_prime(eps: float) -> float:
    return eps / E_0


@np.vectorize
def p_nu(p):
    return E_0 * p


@np.vectorize
def eps_nu(eps):
    return E_0 * eps


def eos_eps(p: float) -> float:
    densities, pressures = EOS_DATA
    eps = np.interp(p, pressures, densities)
    return eps


def eos_eps_prime(p: float):
    densities, pressures = EOS_DATA
    densities, pressures = (eps_prime(densities), p_prime(pressures))
    eps = np.interp(p, pressures, densities)
    return eps
