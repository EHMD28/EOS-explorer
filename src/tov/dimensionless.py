"""
Dimensionless TOV scaling.
"""

from app_constants import ScalingConstants


def pressure_prime(p: float | list[float]) -> float | list[float] | None:
    """
    Convert from pressure in natural units [MeV/fm^3] to a dimensionless
    quantity scaled by `ScalingConstants.E_0`.
    """
    if isinstance(p, float):
        return p / ScalingConstants.EPS_0
    elif isinstance(p, list):
        return [p_i / ScalingConstants.EPS_0 for p_i in p]


def energy_density_prime(eps: float | list[float]) -> float | list[float] | None:
    """
    Convert from energy density in natural units [MeV/fm^3] to a dimensionless
    quantity scaled by `ScalingConstants.E_0`.
    """
    if isinstance(eps, float):
        return eps / ScalingConstants.EPS_0
    elif isinstance(eps, list):
        return [eps_i / ScalingConstants.EPS_0 for eps_i in eps]


def pressure_nu(p_p: float | list[float]) -> float | list[float] | None:
    """
    Convert from a dimensionless quantity scaled by `ScalingConstants.E_0` into
    natural units [MeV/fm^3].
    """
    if isinstance(p_p, float):
        return ScalingConstants.EPS_0 * p_p
    elif isinstance(p_p, list):
        return [ScalingConstants.EPS_0 * p_i for p_i in p_p]


def energy_density_nu(eps_p: float | list[float]) -> float | list[float] | None:
    """
    Convert from a dimensionless quantity scaled by `ScalingConstants.E_0` into
    natural units [MeV/fm^3].
    """
    if isinstance(eps_p, float):
        return ScalingConstants.EPS_0 * eps_p
    elif isinstance(eps_p, list):
        return [ScalingConstants.EPS_0 * eps_i for eps_i in eps_p]


def radius_nu(r_p: float | list[float]) -> float | list[float] | None:
    """
    Convert from a dimensionless quantity scaled by `ScalingConstants.E_0` into
    natural units [km].
    """
    if isinstance(r_p, float):
        return ScalingConstants.A * r_p
    elif isinstance(r_p, list):
        return [ScalingConstants.A * r_i for r_i in r_p]


def mass_nu(m_p: float | list[float]) -> float | list[float] | None:
    """
    Convert from a dimensionless quantity scaled by `ScalingConstants.E_0` into
    natural units [solar masses].
    """
    if isinstance(m_p, float):
        return ScalingConstants.B * m_p
    elif isinstance(m_p, list):
        return [ScalingConstants.B * m_i for m_i in m_p]
