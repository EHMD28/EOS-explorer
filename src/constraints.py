from dataclasses import dataclass
from pathlib import Path
from typing import Literal
from shapely import LineString, Polygon
from matplotlib.axes import Axes
import pandas as pd

type NICER_STEM = Literal["J0740_latest", "J0030", "J0437", "J0614"]
type OBSERVATION_LABEL = Literal["J0740_latest", "J0030", "J0437", "J0614", "GW170817"]


def get_observation_label_from_path(path: Path) -> OBSERVATION_LABEL:
    stem = path.stem  # e.g. "J0740_latest_2sigma"
    if stem.startswith("GW"):
        return "GW170817"
    elif stem.startswith("J0740"):
        return "J0740_latest"
    elif stem.startswith("J0030"):
        return "J0030"
    elif stem.startswith("J0437"):
        return "J0437"
    elif stem.startswith("J0614"):
        return "J0614"
    else:
        raise ValueError(f"Invalid Observation File Path: {path}")


@dataclass
class ObservationalConstraints:
    show_J0740: bool = False
    show_J0030: bool = False
    show_J0437: bool = False
    show_J0614: bool = False
    show_GW170817: bool = False

    def get_value_from_stem(self, stem: NICER_STEM) -> bool:
        match stem:
            case "J0740_latest":
                return self.show_J0740
            case "J0030":
                return self.show_J0030
            case "J0437":
                return self.show_J0437
            case "J0614":
                return self.show_J0614


@dataclass
class ConstraintResults:
    is_consistent_with_J0740: bool = False
    is_consistent_with_J0030: bool = False
    is_consistent_with_J0437: bool = False
    is_consistent_with_J0614: bool = False
    is_consistent_with_GW170817: bool = False


OBSERVATIONS_DIR = Path("data/constraints")

NICER_PULSARS: dict[NICER_STEM, str] = {
    "J0740_latest": "PSR J0740+6620",
    "J0030": "PSR J0030+0451",
    "J0437": "PSR J0437-4715",
    "J0614": "PSR J0614-3329",
}

# Default = 1 sigma only for NICER.
# For 1/2/3 sigma stack use: ['3sigma','2sigma','1sigma']  (outer to inner).
NICER_SIGMAS = ["2sigma"]

# GW170817 default = 90% credible region.
# Available: '1sigma', '2sigma', '3sigma', '90'.
GW_COMPONENTS = ["GW_w_mmax_NS1", "GW_w_mmax_NS2"]
GW_SIGMA_LEVELS = ["90"]

# Styling ---------------------------------------------------------------
STEM_TO_COLOR_MAP = {
    "J0740_latest": "#d62728",
    "J0030": "#1f77b4",
    "J0437": "#2ca02c",
    "J0614": "#9467bd",
}
GW_COLOR = "#7f7f7f"

ALPHA_FOR_LEVEL = {
    "1sigma": 0.55,
    "2sigma": 0.30,
    "3sigma": 0.15,
    "90": 0.35,
}

GW_LABEL_FOR = {
    "1sigma": "GW170817 (68%)",
    "2sigma": "GW170817 (95%)",
    "3sigma": "GW170817 (99.7%)",
    "90": "GW170817 (90%)",
}


def get_all_observation_file_paths(
    include_nicer: bool = True, include_gw: bool = True
) -> list[Path]:
    paths: list[Path] = []
    # Find all NICER observations paths
    if include_nicer:
        for stem in NICER_PULSARS.keys():
            for sigma in NICER_SIGMAS:
                path = OBSERVATIONS_DIR.joinpath(f"{stem}_{sigma}.csv")
                paths.append(path)
    # Find all gravitational-wave observations paths
    if include_gw:
        for comp in GW_COMPONENTS:
            for sigma in GW_SIGMA_LEVELS:
                path = OBSERVATIONS_DIR.joinpath(f"{comp}_{sigma}.csv")
                paths.append(path)
    return paths


def get_observation_file_path(stem: str, sigma: str):
    return OBSERVATIONS_DIR.joinpath(f"{stem}_{sigma}.csv")


def load_constraint_region(path: Path):
    return pd.read_csv(path)


def plot_nicer_constraints(ax: Axes, constraints: ObservationalConstraints):
    """
    Plot the NICER constraints to `ax`. Returns an `ObservationalConstraints`
    to indicate if each of the observational constraints is being meet.
    """

    for stem, label in NICER_PULSARS.items():
        color = STEM_TO_COLOR_MAP[stem]
        for sigma in NICER_SIGMAS:
            show_region: bool = constraints.get_value_from_stem(stem)
            if show_region:
                file_path = get_observation_file_path(stem, sigma)
                df = load_constraint_region(file_path)
                ax.fill(
                    df["R_km"],
                    df["M_solar"],
                    color=color,
                    alpha=ALPHA_FOR_LEVEL[sigma],
                    label=label if sigma == NICER_SIGMAS[-1] else None,
                    edgecolor=color,
                    linewidth=1.0,
                )


def plot_gw170817_constraints(ax: Axes, constraints: ObservationalConstraints):
    if constraints.show_GW170817:
        for i, comp in enumerate(GW_COMPONENTS):
            for sigma in GW_SIGMA_LEVELS:
                file_path = get_observation_file_path(comp, sigma)
                df = load_constraint_region(file_path)
                ax.fill(
                    df["R_km"],
                    df["M_solar"],
                    color=GW_COLOR,
                    alpha=ALPHA_FOR_LEVEL[sigma],
                    edgecolor=GW_COLOR,
                    linewidth=1.0,
                    label=GW_LABEL_FOR[sigma] if (i == 0) else None,
                )


def get_constraint_results_from_mr_curve(
    mr_curve_points: list[tuple[float, float]],
) -> ConstraintResults:
    results = ConstraintResults()
    contours_dict: dict[OBSERVATION_LABEL, Polygon] = {}
    observation_paths = get_all_observation_file_paths()
    for path in observation_paths:
        label = get_observation_label_from_path(path)
        df = pd.read_csv(path)
        contour = Polygon(zip(df["R_km"], df["M_solar"]))
        contours_dict[label] = contour
    mr_curve = LineString(mr_curve_points)
    # TODO: Refactor into dictionary
    if mr_curve.intersects(contours_dict["J0740_latest"]):
        results.is_consistent_with_J0740 = True
    if mr_curve.intersects(contours_dict["J0030"]):
        results.is_consistent_with_J0030 = True
    if mr_curve.intersects(contours_dict["J0437"]):
        results.is_consistent_with_J0437 = True
    if mr_curve.intersects(contours_dict["J0614"]):
        results.is_consistent_with_J0614 = True
    if mr_curve.intersects(contours_dict["GW170817"]):
        results.is_consistent_with_GW170817 = True
    return results
