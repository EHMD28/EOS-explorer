import numpy as np

from app_constants import ScalingConstants


@np.vectorize
def pressure_prime(p: float) -> float:
    return p / ScalingConstants.E_0


@np.vectorize
def energy_density_prime(eps: float) -> float:
    return eps / ScalingConstants.E_0


@np.vectorize
def pressure_nu(p_p):
    return ScalingConstants.E_0 * p_p


@np.vectorize
def energy_density_nu(eps_p):
    return ScalingConstants.E_0 * eps_p


@np.vectorize
def radius_nu(r_p: float) -> float:
    return ScalingConstants.A * r_p


@np.vectorize
def mass_nu(m_p: float) -> float:
    return ScalingConstants.B * m_p
