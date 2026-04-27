from dataclasses import dataclass
import os
from typing import Literal
from matplotlib.axes import Axes
import pandas as pd


@dataclass
class ObservationalConstraints:
    show_J0740: bool = False
    show_J0030: bool = False
    show_J0437: bool = False
    show_J0614: bool = False
    show_GW170817: bool = False


DATA = "data/constraints"

# Which pulsars, GW components, and levels to draw ----------------------
NICER_STEM = Literal["J0740_latest", "J0030", "J0437", "J0614"]

nicer_pulsars: dict[NICER_STEM, str] = {
    "J0740_latest": "PSR J0740+6620",
    "J0030": "PSR J0030+0451",
    "J0437": "PSR J0437-4715",
    "J0614": "PSR J0614-3329",
}

# Default = 1 sigma only for NICER.
# For 1/2/3 sigma stack use: ['3sigma','2sigma','1sigma']  (outer to inner).
nicer_sigmas = ["2sigma"]

# GW170817 default = 90% credible region.
# Available: '1sigma', '2sigma', '3sigma', '90'.
gw_components = ["GW_w_mmax_NS1", "GW_w_mmax_NS2"]
gw_levels = ["90"]

# Styling ---------------------------------------------------------------
stemp_to_color_map = {
    "J0740_latest": "#d62728",
    "J0030": "#1f77b4",
    "J0437": "#2ca02c",
    "J0614": "#9467bd",
}
gw_color = "#7f7f7f"

alpha_for_level = {
    "1sigma": 0.55,
    "2sigma": 0.30,
    "3sigma": 0.15,
    "90": 0.35,
}

gw_label_for = {
    "1sigma": "GW170817 (68%)",
    "2sigma": "GW170817 (95%)",
    "3sigma": "GW170817 (99.7%)",
    "90": "GW170817 (90%)",
}


def load_constraint_region(name: str):
    return pd.read_csv(os.path.join(DATA, name + ".csv"))


def plot_nicer_constraints(ax: Axes, constraints: ObservationalConstraints):
    for stem, label in nicer_pulsars.items():
        color = stemp_to_color_map[stem]
        for sigma in nicer_sigmas:
            show_region: bool = False
            match stem:
                case "J0740_latest":
                    show_region = constraints.show_J0740
                case "J0030":
                    show_region = constraints.show_J0030
                case "J0437":
                    show_region = constraints.show_J0437
                case "J0614":
                    show_region = constraints.show_J0614
            if show_region:
                df = load_constraint_region(f"{stem}_{sigma}")
                ax.fill(
                    df["R_km"],
                    df["M_solar"],
                    color=color,
                    alpha=alpha_for_level[sigma],
                    label=label if sigma == nicer_sigmas[-1] else None,
                    edgecolor=color,
                    linewidth=1.0,
                )


def plot_gw170817_constraints(ax: Axes):
    for i, comp in enumerate(gw_components):
        for s in gw_levels:
            df = load_constraint_region(f"{comp}_{s}")
            ax.fill(
                df["R_km"],
                df["M_solar"],
                color=gw_color,
                alpha=alpha_for_level[s],
                edgecolor=gw_color,
                linewidth=1.0,
                label=gw_label_for[s] if (i == 0) else None,
            )
