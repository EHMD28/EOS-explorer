from typing import Literal
import typing

import numpy as np
import streamlit as st

from eos.polytropic import eos_p_vec as polytropic_eos_p
from plotting import generate_log_fig

EOS_OPTIONS = Literal["Polytropic", "Speed-of-Sound Interpolation"]


def draw_and_get_eos_dropdown() -> EOS_OPTIONS:
    valid_options = typing.get_args(EOS_OPTIONS)
    # The pyright ignore statement is because Streamlit's return type isn't
    # technically correct.
    option: EOS_OPTIONS = st.selectbox("Choose an EOS", valid_options)  # pyright: ignore[reportAssignmentType]
    return option


# -------------------- Polytropic Equation of State --------------------


def draw_info_for_polytropic_eos():
    st.markdown("# Polytropic Equation of State")
    st.latex(r"P(\varepsilon) = K\varepsilon^\gamma")
    st.markdown(r"$P(\varepsilon)$ = Pressure in _MeV/fm^3_")
    st.markdown(r"$\varepsilon$ = Energy density in _MeV/fm^3_")
    st.markdown(
        r"$\Kappa$ = Proportionality Constant. The dimension of $K$ cancels out the dimension of $\varepsilon^\gamma$"
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
    Returns a tuple containing the chosen values of the parameters in the form
    (kappa, gamma).
    """
    st.markdown("# Parameters")
    kappa = st.number_input(
        label="K - Proportionality Constant",
        # Min and max value are arbitary. Might change/remove them later.
        min_value=1e-10,
        max_value=5.0,
        value=1.0,
    )
    gamma = st.number_input(
        label="𝛾 - Stiffness Value",
        # Min and max value are arbitary. Might change/remove them later.
        min_value=-1.0,
        max_value=10.0,
        value=1.0,
    )
    return (kappa, gamma)


def draw_and_get_density_range_for_polytropic_eos() -> tuple[float, float]:
    """
    Returns a tuple containing the chosen range of energy density magnitude values.
    """
    eps_start, eps_end = st.slider(
        label=r"$\varepsilon$ Magnitude Range - Evaluation Range: [$10^{start}$, $10^{end}$)",
        # Min and max value are arbitary. Might change/remove them later.
        min_value=-20,
        max_value=10,
        value=(1, 5),
    )
    return (eps_start, eps_end)


def draw_polytropic_eos_plot(
    kappa: float, gamma: float, eps_magnitudes: tuple[float, float]
):
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
    st.pyplot(fig)


def draw_and_get_eos_data_upload():
    file = st.file_uploader(label="Choose a data file", type=["txt", "csv", "tsv"])


def draw_ui_for_polytropic_eos():
    draw_info_for_polytropic_eos()
    col_one, col_two = st.columns(spec=[0.4, 0.6])
    with col_one:
        kappa, gamma = draw_and_get_parameters_for_polytropic_eos()
        eps_start, eps_end = draw_and_get_density_range_for_polytropic_eos()
        draw_and_get_eos_data_upload()
    with col_two:
        draw_polytropic_eos_plot(kappa, gamma, eps_magnitudes=(eps_start, eps_end))


# def plot_tabulated_eos():
#     densities, pressures = EOS_DATA
#     eos_fig = generate_log_fig(
#         densities,
#         pressures,
#         title="Tabulated EoS",
#         x_label="Energy Density [MeV/fm^3]",
#         y_label="Pressure [MeV/fm^3]",
#         is_scatter=True,
#     )
#     st.pyplot(eos_fig)


# def plot_lin_tabulated_eos():
#     densities, pressures = EOS_DATA
#     fig, ax = plt.subplots()
#     ax.set_title("Linearly-Spaced EOS")
#     ax.set_xlabel("Energy Density [MeV/fm^3]")
#     ax.set_ylabel("Pressure [MeV/fm^3]")
#     ax.scatter(densities, pressures)
#     st.pyplot(fig)


# def plot_tabulated_mr():
#     radii, masses = MR_DATA
#     mr_fig = generate_log_fig(
#         radii,
#         masses,
#         title="Tabulated Mass-Radius Curve",
#         x_label="Radius [km]",
#         y_label="Mass [M☉]",
#         is_scatter=True,
#     )
#     mr_ax = mr_fig.axes[0]
#     mr_ax.plot(radii, masses, color="orange")
#     st.pyplot(mr_fig)


# def plot_lin_tabulated_mr():
#     radii, masses = MR_DATA
#     lin_mr_fig, lin_mr_ax = plt.subplots()
#     lin_mr_ax.scatter(radii, masses)
#     lin_mr_ax.set_title("Linearly-Spaced Mass-Radius Curve")
#     lin_mr_ax.set_xlabel("Radius [km]")
#     lin_mr_ax.set_ylabel("Mass [M☉]")
#     st.pyplot(lin_mr_fig)


def draw_ui_for_soc_eos():
    st.text("Work In Progress")


def draw_ui():
    eos_dropdown = draw_and_get_eos_dropdown()
    match eos_dropdown:
        case "Polytropic":
            draw_ui_for_polytropic_eos()
        case "Speed-of-Sound Interpolation":
            draw_ui_for_soc_eos()
