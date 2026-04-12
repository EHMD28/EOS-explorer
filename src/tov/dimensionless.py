"""
Dimensionless TOV scaling.
"""

import typing

from app_constants import ScalingConstants


def energy_density_unit_prime(n_nu: float | list[float]) -> float | list[float] | None:
    if isinstance(n_nu, (float, int)):
        return n_nu / ScalingConstants.EPS_0
    elif isinstance(n_nu, list):
        return [n_i / ScalingConstants.EPS_0 for n_i in n_nu]


def energy_density_unit_nu(n_p: float | list[float]) -> float | list[float] | None:
    if isinstance(n_p, (float, int)):
        return ScalingConstants.EPS_0 * n_p
    elif isinstance(n_p, list):
        return [ScalingConstants.EPS_0 * n_i for n_i in n_p]


@typing.overload
def pressure_prime(p_nu: float) -> float: ...


@typing.overload
def pressure_prime(p_nu: list[float]) -> list[float]: ...


def pressure_prime(p_nu: float | list[float]) -> float | list[float] | None:
    """
    Convert from pressure in natural units [MeV/fm^3] to a dimensionless
    quantity scaled by `ScalingConstants.EPS_0`.
    """
    return energy_density_unit_prime(p_nu)


@typing.overload
def energy_density_prime(eps_nu: float) -> float: ...


@typing.overload
def energy_density_prime(eps_nu: list[float]) -> list[float]: ...


def energy_density_prime(eps_nu: float | list[float]) -> float | list[float] | None:
    """
    Convert from energy density in natural units [MeV/fm^3] to a dimensionless
    quantity scaled by `ScalingConstants.EPS_0`.
    """
    return energy_density_unit_prime(eps_nu)


@typing.overload
def pressure_nu(p_p: float) -> float: ...


@typing.overload
def pressure_nu(p_p: list[float]) -> list[float]: ...


def pressure_nu(p_p: float | list[float]) -> float | list[float] | None:
    """
    Convert from a dimensionless quantity scaled by `ScalingConstants.EPS_0` into
    natural units [MeV/fm^3].
    """
    return energy_density_unit_nu(p_p)


def energy_density_nu(eps_p: float | list[float]) -> float | list[float] | None:
    """
    Convert from a dimensionless quantity scaled by `ScalingConstants.EPS_0` into
    natural units [MeV/fm^3].
    """
    return energy_density_unit_nu(eps_p)


@typing.overload
def radius_nu(r_p: float) -> float: ...


@typing.overload
def radius_nu(r_p: list[float]) -> list[float]: ...


def radius_nu(r_p: float | list[float]) -> float | list[float] | None:
    """
    Convert from a dimensionless quantity scaled by `ScalingConstants.EPS_0` into
    natural units [km].
    """
    if isinstance(r_p, (float, int)):
        return ScalingConstants.A * r_p
    elif isinstance(r_p, list):
        return [ScalingConstants.A * r_i for r_i in r_p]


@typing.overload
def mass_nu(m_p: float) -> float: ...


@typing.overload
def mass_nu(m_p: list[float]) -> list[float]: ...


def mass_nu(m_p: float | list[float]) -> float | list[float] | None:
    """
    Convert from a dimensionless quantity scaled by `ScalingConstants.EPS_0` into
    natural units [solar masses].
    """
    if isinstance(m_p, (float, int)):
        return ScalingConstants.B * m_p
    elif isinstance(m_p, list):
        return [ScalingConstants.B * m_i for m_i in m_p]
