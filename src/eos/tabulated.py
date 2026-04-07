from io import TextIOWrapper
from pathlib import Path
from typing import TextIO

import pandas as pd


def load_df_from_path(path: Path, sep: str) -> pd.DataFrame:
    """Loads the data from a `sep`-separated values file, ignoring any lines at the start of the
    file that begin with a '#'.


    Args:
        path (Path): Path to file.
        sep (str): Column separator (should be either tab, space, or comma).

    Returns:
        pd.DataFrame: Dataframe loaded from the file.
    """
    with open(path, "r") as f:
        # Skip over all of the comments at the start of the file.
        pos = 0
        while f.readline().startswith("#"):
            pos = f.tell()
        f.seek(pos)
        df = pd.read_table(f, sep=sep)
    return df


def load_eos_from_file(path: Path) -> tuple[list[float], list[float]]:
    """Extracts the pressures and energy densities from a `DataFrame` with the columns p (pressure
    in MeV/fm^3) and e (energy density in MeV/fm^3).

    Args:
        path (Path): Path to file.

    Returns:
        tuple[list[float], list[float]]: A tuple of the form (energy_densities, pressures).
    """
    df = load_df_from_path(path, sep="\t")
    pressures: pd.Series[float] = df["p"]
    energy_densities: pd.Series[float] = df["e"]
    return (energy_densities.tolist(), pressures.tolist())


def load_mr_curve_from_df(path: Path) -> tuple[list[float], list[float]]:
    """Extracts the masses and radii from a `DataFrame` with columns m (mass in solar masses) and
    r (radius in km).

    Args:
        path (Path): Path to file.

    Returns:
        tuple[list[float], list[float]]: A tuple of the form (radii, masses).
    """
    df = load_df_from_path(path, sep=" ")
    masses: pd.Series[float] = df["m"]
    radii: pd.Series[float] = df["r"]
    return (radii.tolist(), masses.tolist())


# def get_dimensionless_data():
#     densities, pressures = EOS_DATA
#     densities = [eps * ScalingConstants.MEV_PER_FM3_TO_SM_PER_KM_3 for eps in densities]
#     densities, pressures = (energy_density_prime(densities), pressure_prime(pressures))
#     return (densities, pressures)


# DIMENSIONLESS_DATA = get_dimensionless_data()


# def eos_eps_prime(p: float):
#     pressures, densities = DIMENSIONLESS_DATA
#     eps = np.interp(p, pressures, densities)
#     return eps
