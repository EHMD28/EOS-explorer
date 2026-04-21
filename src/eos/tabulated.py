"""
Tabulated EoS handling.
"""

import csv
from typing import TextIO

import numpy as np
import pandas as pd


class LogarithmicInterpolator:
    """
    A wrapper around NumPy's `interp` function designed for handling data that
    spans multiple orders of magntidue. Internally, the class converts
    everything into a more "fittable" form by using `log10`.
    """

    def __init__(self, x_values: list[float], y_values: list[float]) -> None:
        self._log_x = np.log10(x_values)
        self._log_y = np.log10(y_values)

    def get_y(self, x_in):
        """
        Returns the interpolated y-value(s) for a given x-value(s).
        """
        log_y_out = np.interp(np.log10(x_in), self._log_x, self._log_y)
        return 10**log_y_out


def load_eos_from_file(data_file: TextIO) -> tuple[list[float], list[float]] | None:
    """
    Extracts the pressures and energy densities from `data_file`. This function
    assumes that `data_file` has a header row with columns p (pressure [MeV/fm^3])
    and e (energy density [MeV/fm^3]). Also, any non-data rows must be prefixed
    with '#'. If there are any issues, this function will return `None`.

    This function should be able to handle any delimeter, but commas or tabs are
    preferred.
    """
    df = pd.read_csv(data_file, sep=None, header="infer", comment="#", engine="python")
    header = df.columns.values
    if "p" in header and "e" in header:
        pressures: pd.Series[float] = df["p"]
        energy_densities: pd.Series[float] = df["e"]
        return (energy_densities.tolist(), pressures.tolist())
    else:
        return None


def load_mr_curve_from_file(
    data_file: TextIO,
) -> tuple[list[float], list[float]] | None:
    """
    Extracts the masses and radii from `data_file`. This function
    assumes that `data_file` has a header row with columns m (mass [solar masses])
    and r (radius [km]). Also, any non-data rows must be prefixed
    with '#'. If there are any issues, this function will return `None`.

    This function should be able to handle any delimeter, but commas or tabs are
    preferred.
    """
    df = pd.read_csv(data_file, sep=None, header="infer", comment="#", engine="python")
    header = df.columns.values
    if "m" in header and "r" in header:
        masses: pd.Series[float] = df["m"]
        radii: pd.Series[float] = df["r"]
        return (radii.tolist(), masses.tolist())
    else:
        return None


def interpolate_eps(p: float, densities: list[float], pressures: list[float]) -> float:
    """
    Interpolate EoS using `densities` and `pressures`. All quantities should have
    a unit of MeV/fm^3 using NumPy's interpolation method.
    """
    log_p = np.log10(pressures)
    log_eps = np.log10(densities)
    p_in = np.log10(p)
    log_eps_out = np.interp(p_in, log_p, log_eps)
    return 10**log_eps_out
