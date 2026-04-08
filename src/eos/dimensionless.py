"""
Dimensionless TOV scaling.
"""

import numpy as np

from app_constants import ScalingConstants


@np.vectorize
def pressure_prime(p: float) -> float:
    """
    Convert from pressure in natural units [MeV/fm^3] to a dimensionless
    quantity scaled by `ScalingConstants.E_0`.
    """
    return p / ScalingConstants.E_0


@np.vectorize
def energy_density_prime(eps: float) -> float:
    """
    Convert from energy density in natural units [MeV/fm^3] to a dimensionless
    quantity scaled by `ScalingConstants.E_0`.
    """
    return eps / ScalingConstants.E_0


@np.vectorize
def pressure_nu(p_p):
    """
    Convert from a dimensionless quantity scaled by `ScalingConstants.E_0` into
    natural units [MeV/fm^3].
    """
    return ScalingConstants.E_0 * p_p


@np.vectorize
def energy_density_nu(eps_p):
    """
    Convert from a dimensionless quantity scaled by `ScalingConstants.E_0` into
    natural units [MeV/fm^3].
    """
    return ScalingConstants.E_0 * eps_p


@np.vectorize
def radius_nu(r_p: float) -> float:
    """
    Convert from a dimensionless quantity scaled by `ScalingConstants.E_0` into
    natural units [km].
    """
    return ScalingConstants.A * r_p


@np.vectorize
def mass_nu(m_p: float) -> float:
    """
    Convert from a dimensionless quantity scaled by `ScalingConstants.E_0` into
    natural units [solar masses].
    """
    return ScalingConstants.B * m_p
