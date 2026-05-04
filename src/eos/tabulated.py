"""
Tabulated EoS handling.
"""

from typing import Literal, TextIO
import typing

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


ALLOWED_FILE_EXTENSIONS = Literal["txt", "csv", "tsv"]


def get_allowed_file_extensions():
    return typing.get_args(ALLOWED_FILE_EXTENSIONS)


EXTENSION_TO_DELIMETER_MAP: dict[ALLOWED_FILE_EXTENSIONS, str] = {
    "txt": " ",
    "csv": ",",
    "tsv": "\t",
}


def load_eos_from_file(
    data_file: TextIO, extension: ALLOWED_FILE_EXTENSIONS
) -> tuple[list[float], list[float]] | None:
    """
    Extracts EoS data from a file-like object. Assumes file has the columns 'p'
    for pressure in MeV/fm^3 and 'e' for energy density in MeV/fm^3. The
    delimeter is inferred from the file extension.
    """
    data_file.seek(0)
    sep = EXTENSION_TO_DELIMETER_MAP[extension]
    df = pd.read_csv(data_file, sep=sep, header="infer", comment="#")
    header = df.columns.values
    if "p" in header and "e" in header:
        pressures: pd.Series[float] = df["p"]
        energy_densities: pd.Series[float] = df["e"]
        return (energy_densities.tolist(), pressures.tolist())
    else:
        return None


def load_mr_curve_from_file(
    data_file: TextIO, extension: ALLOWED_FILE_EXTENSIONS
) -> tuple[list[float], list[float]] | None:
    """
    Extracts mass-radius curve data from a file-like object. Assumes file has
    the columns 'r' for radius in km and 'm' for mass in solar masses. The
    delimeter is inferred from the file extension.
    """
    data_file.seek(0)
    sep = EXTENSION_TO_DELIMETER_MAP[extension]
    df = pd.read_csv(data_file, sep=sep, header="infer", comment="#")
    header = df.columns.values
    if "m" in header and "r" in header:
        masses: pd.Series[float] = df["m"]
        radii: pd.Series[float] = df["r"]
        return (radii.tolist(), masses.tolist())
    else:
        return None
