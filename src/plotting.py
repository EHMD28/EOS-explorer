from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd


def load_df_from_file(path: Path, sep: str) -> pd.DataFrame:
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
    df = load_df_from_file(path, sep="\t")
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
    df = load_df_from_file(path, sep=" ")
    masses: pd.Series[float] = df["m"]
    radii: pd.Series[float] = df["r"]
    return (radii.tolist(), masses.tolist())


def generate_log_fig(
    xs: list[float],
    ys: list[float],
    title: str = "",
    x_label: str = "",
    y_label: str = "",
    is_scatter: bool = False,
) -> Figure:
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xscale("log")
    ax.set_yscale("log")
    if is_scatter:
        ax.scatter(xs, ys)
    else:
        ax.plot(xs, ys)
    fig.add_axes(ax)
    return fig
