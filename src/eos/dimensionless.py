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
