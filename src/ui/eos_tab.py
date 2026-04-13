"""
All user interface code.
"""

import typing
from typing import Literal

import numpy as np
import pandas as pd
import streamlit as st

from app_constants import DebugConstants
from eos.polytropic import eos_eps as polytropic_eos_eps
from eos.polytropic import eos_p as polytropic_eos_p
from eos.tabulated import load_mr_curve_from_file
from plotting import generate_log_fig
from tov.solver import EOS_EPS_FN_TYPE, generate_mass_radius_curve

EOS_OPTIONS_TYPE = Literal["Polytropic", "Speed-of-Sound Interpolation"]


def draw_and_get_eos_dropdown() -> EOS_OPTIONS_TYPE:
    """
    Write EoS selection dropdown to the UI and get the selected option.
    """
    valid_options = typing.get_args(EOS_OPTIONS_TYPE)
    # The pyright ignore statement is because Streamlit's return type isn't
    # technically correct.
    option: EOS_OPTIONS_TYPE = st.selectbox("Choose an EoS", valid_options)  # pyright: ignore[reportAssignmentType]
    return option


# -------------------- Polytropic Equation of State --------------------


def draw_info_for_polytropic_eos():
    """
    Write relevant information for the polytropic EoS to the UI.
    """
    st.markdown("# Polytropic Equation of State")
    st.latex(r"P(\varepsilon) = K\varepsilon^\gamma.")
    st.markdown(r"$P(\varepsilon)$ = Pressure in _MeV/fm^3_.")
    st.markdown(r"$\varepsilon$ = Energy density in _MeV/fm^3_.")
    st.markdown(
        r"$\Kappa$ = Proportionality Constant. The dimension of $K$ cancels out the dimension of $\varepsilon^\gamma$."
    )
    st.markdown(r"$\gamma$ = Polytropic Index (dimensionless) ")
    st.text(
        "Note that, using the rules of logarithms, the equation can be rearranged to the following form."
    )
    st.latex(r"\log(P) = \gamma \log(\varepsilon) + \log(K)")
    st.markdown(
        r'Note that this equation is structurally identical to the equation of a line in slope-intercept form ($y = mx+b$), assuming $y = \log(P)$, $x = \log(\varepsilon)$, and $b = \log(K)$. From this observation, it is evident that $\gamma$ is the "logarithmic slope" of $P$ with respect to $\varepsilon$.  '
    )


def draw_and_get_parameters_for_polytropic_eos() -> tuple[float, float]:
    """
    Write the parameter sliders to the UI. Returns a tuple containing the chosen
    values of the parameters in the form (kappa, gamma).
    """
    st.markdown("# Parameters ")
    kappa = st.number_input(
        label="K - Proportionality Constant",
        # Min and max value are arbitary. Might change/remove them later.
        min_value=1e-10,
        max_value=5.0,
        value=DebugConstants.MID_DENSITY_KAPPA,  # TODO: Change to a reasonable default
        format="%e",
    )
    gamma = st.number_input(
        label="𝛾 - Stiffness Value",
        # Min and max value are arbitary. Might change/remove them later.
        min_value=-1.0,
        max_value=10.0,
        value=DebugConstants.MID_DENSITY_GAMMA,  # TODO: Change to a reasonable default
        format="%.10f",
    )
    return (kappa, gamma)


def draw_and_get_density_range_for_polytropic_eos() -> tuple[float, float]:
    """
    Write the energy density range slider to the UI. Returns a tuple containing
    the chosen range of energy density order of magnitude values.
    """
    eps_start, eps_end = st.slider(
        label=r"$\varepsilon$ Magnitude Range - Evaluation Range: $[10^{start}, 10^{end})$",
        # Min and max value are arbitary. Might change/remove them later.
        min_value=-20,
        max_value=10,
        value=(-5, 5),
    )
    return (eps_start, eps_end)


def draw_and_get_eos_data_from_upload() -> tuple[list[float], list[float]] | None:
    """
    Write the EoS file upload option to the UI. Returns a tuple of the form
    (densities, pressure) if a file of the correct format was uploaded, otherwise
    None.
    """
    uploaded_file = st.file_uploader(
        label="Choose an EoS data file", type=["txt", "csv", "tsv"]
    )
    # TODO: Move to appropriate file
    if uploaded_file is not None:
        df = pd.read_csv(
            uploaded_file, sep=None, header="infer", comment="#", engine="python"
        )
        header = df.columns.values.tolist()
        if "p" in header and "e" in header:
            pressures = df["p"]
            densities = df["e"]
            return (densities.tolist(), pressures.tolist())
    return None


def draw_polytropic_eos_plot(
    kappa: float,
    gamma: float,
    eps_magnitudes: tuple[float, float],
    tabulated_densities: list[float] | None = None,
    tabulated_pressures: list[float] | None = None,
):
    """
    Write the EoS plot to the UI using the chosen parameters. If `densities` and
    `pressures` (from a tabulated EoS) are included, then it will plot those as
    points.
    """
    eps_start, eps_end = eps_magnitudes
    eps_range = np.logspace(eps_start, eps_end, num=200)
    p_values = polytropic_eos_p(eps_range.tolist(), kappa, gamma)
    fig = generate_log_fig(
        xs=eps_range.tolist(),
        ys=p_values,
        title="Pressure vs. Energy Density",
        x_label="Energy Density [MeV/fm^3]",
        y_label="Pressure [MeV/fm^3]",
    )
    if tabulated_densities is not None and tabulated_pressures is not None:
        ax = fig.axes[0]
        ax.scatter(tabulated_densities, tabulated_pressures, color="orange")
    st.pyplot(fig)


# -------------------- General UI --------------------


def draw_and_get_pressure_range() -> tuple[float, float]:
    """
    Write the pressure range slider to the UI. Returns a tuple containing
    the chosen orders of magnitude for pressure [MeV/fm^3] in the form
    (start, end).
    """
    p_start, p_end = st.slider(
        label=r"$P$ Magnitude Range - Evaluation Range: $[10^{start}, 10^{end})$",
        # Min and max value are arbitary. Might change/remove them later.
        min_value=-20,
        max_value=20,
        value=(0, 4),
    )
    return (p_start, p_end)


def draw_mass_radius_curve(
    radii: list[float],
    masses: list[float],
    tabulated_radii: list[float] | None = None,
    tabulated_masses: list[float] | None = None,
):
    """
    Write the mass-radius curve plot to the UI using the chosen parameters. If
    `tabulated_radii` and `tabulated_masses` are included, then it will plot
    those as points.
    """
    fig = generate_log_fig(
        radii,
        masses,
        title="Mass-Radius Curve",
        x_label="Radius [km]",
        y_label="Masses [M_sun]",
        is_scatter=True,
    )
    if tabulated_radii is not None and tabulated_masses is not None:
        ax = fig.axes[0]
        ax.scatter(tabulated_radii, tabulated_masses)
    empty_col_1, plot_col, epmty_col2 = st.columns([1, 3, 1])
    with plot_col:
        st.pyplot(fig)


def draw_ui_for_polytropic_eos():
    """
    Write all components to the UI for a polytropic EoS.
    """
    draw_info_for_polytropic_eos()
    col_one, col_two = st.columns(spec=[0.4, 0.6])
    with col_one:
        kappa, gamma = draw_and_get_parameters_for_polytropic_eos()
        eps_start, eps_end = draw_and_get_density_range_for_polytropic_eos()
        data = draw_and_get_eos_data_from_upload()
        densities, pressures = data if data is not None else (None, None)
    with col_two:
        draw_polytropic_eos_plot(
            kappa,
            gamma,
            eps_magnitudes=(eps_start, eps_end),
            tabulated_densities=densities,
            tabulated_pressures=pressures,
        )
    draw_ui_for_mass_radius_curve(
        eos_eps_fn=lambda p: polytropic_eos_eps(p, kappa, gamma)
    )


def draw_ui_for_soc_eos():
    st.text("Work In Progress")


def draw_and_get_mr_data_from_upload() -> tuple[list[float], list[float]] | None:
    """
    Write the mass-radius curve file upload option to the UI. Returns a tuple of
    the form (radii, masses) if a file of the correct format was uploaded, otherwise
    None.
    """
    uploaded_file = st.file_uploader(
        label="Choose a mass-radius data file", type=["txt", "csv", "tsv"]
    )
    if uploaded_file is not None:
        return load_mr_curve_from_file(uploaded_file)  # pyright: ignore[reportArgumentType]
    else:
        return None


def draw_ui_for_mass_radius_curve(eos_eps_fn: EOS_EPS_FN_TYPE):
    p_start, p_end = draw_and_get_pressure_range()
    radii, masses = generate_mass_radius_curve(
        p_c_magnitude_range=(p_start, p_end), eos_eps_fn=eos_eps_fn
    )
    data = draw_and_get_mr_data_from_upload()
    if data is not None:
        tabulated_radii, tabulated_masses = data
        draw_mass_radius_curve(radii, masses, tabulated_radii, tabulated_masses)
    else:
        draw_mass_radius_curve(radii, masses)
