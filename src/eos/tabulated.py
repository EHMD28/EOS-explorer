import numpy as np

from app_constants import EOS_DATA, ScalingConstants
from eos.dimensionless import eps_prime, p_prime


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
