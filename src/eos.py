import numpy as np

from app_constants import EOS_DATA, ScalingConstants


@np.vectorize
def p_prime(p: float) -> float:
    return p / ScalingConstants.E_0


@np.vectorize
def eps_prime(eps: float) -> float:
    return eps / ScalingConstants.E_0


@np.vectorize
def p_nu(p_p):
    return ScalingConstants.E_0 * p_p


@np.vectorize
def eps_nu(eps_p):
    return ScalingConstants.E_0 * eps_p


@np.vectorize
def r_nu(r_p: float) -> float:
    return ScalingConstants.A * r_p


@np.vectorize
def m_nu(m_p: float) -> float:
    return ScalingConstants.B * m_p


def eos_eps(p: float) -> float:
    densities, pressures = EOS_DATA
    eps = np.interp(p, pressures, densities)
    return eps


def get_dimensionless_data():
    densities, pressures = EOS_DATA
    densities = [eps * ScalingConstants.MEV_PER_FM3_TO_SM_PER_KM_3 for eps in densities]
    densities, pressures = (eps_prime(densities), p_prime(pressures))
    return (densities, pressures)


DIMENSIONLESS_DATA = get_dimensionless_data()


def eos_eps_prime(p: float):
    pressures, densities = DIMENSIONLESS_DATA
    eps = np.interp(p, pressures, densities)
    return eps
