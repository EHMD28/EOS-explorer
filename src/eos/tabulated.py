"""
Tabulated EoS handling.
"""

from typing import TextIO

import pandas as pd


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


def load_mr_curve_from_df(data_file: TextIO) -> tuple[list[float], list[float]] | None:
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
