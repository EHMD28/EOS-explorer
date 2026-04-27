"""
All user interface code.
"""

from dataclasses import dataclass
import typing

from matplotlib import pyplot as plt
import numpy as np
import streamlit as st

from app_constants import DebugConstants, StreamlitKeys, UiConstants
from constraints import (
    ObservationalConstraints,
    plot_gw170817_constraints,
    plot_nicer_constraints,
)
from eos.polytropic import eos_eps as polytropic_eos_eps
from eos.polytropic import eos_p as polytropic_eos_p
from eos.tabulated import (
    LogarithmicInterpolator,
    load_eos_from_file,
    load_mr_curve_from_file,
)
from tov.solver import EOS_EPS_FN_TYPE, generate_mass_radius_curve

# -------------------- Types --------------------

EOS_OPTIONS_TYPE = typing.Literal[
    "Polytropic", "Tabulated", "Speed-of-Sound Interpolation"
]

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


def draw_polytropic_parameters_inputs():
    """
    Write the parameter sliders to the UI. Returns a tuple containing the chosen
    values of the parameters in the form (kappa, gamma).
    """
    st.markdown("## Parameters ")
    st.number_input(
        label="K - Proportionality Constant",
        # Min and max value are arbitary. Might change/remove them later.
        min_value=1e-10,
        max_value=5.0,
        value=DebugConstants.MID_DENSITY_KAPPA,  # TODO: Change to a reasonable default
        format="%e",
        key=StreamlitKeys.POLYTROPIC_EOS_KAPPA_INPUT,
    )
    st.number_input(
        label="𝛾 - Stiffness Value",
        # Min and max value are arbitary. Might change/remove them later.
        min_value=-1.0,
        max_value=10.0,
        value=DebugConstants.MID_DENSITY_GAMMA,  # TODO: Change to a reasonable default
        format="%.10f",
        key=StreamlitKeys.POLYTROPIC_EOS_GAMMA_INPUT,
    )


def draw_density_range_slider():
    """
    Write the energy density range slider to the UI. Returns a tuple containing
    the chosen range of energy density order of magnitude values.
    """
    st.slider(
        label=r"$\varepsilon$ Magnitude Range - Evaluation Range: $[10^{start}, 10^{end})$",
        # Min and max value are arbitary. Might change/remove them later.
        min_value=-20,
        max_value=10,
        value=(-5, 5),
        key=StreamlitKeys.ENERGY_DENSITY_SLIDER,
    )


def draw_eos_file_upload_widget() -> tuple[list[float], list[float]] | None:
    """
    Write the EoS file upload option to the UI. Returns a tuple of the form
    (densities, pressure) if a file of the correct format was uploaded, otherwise
    None.
    """
    st.file_uploader(
        label="Choose an EoS data file",
        type=["txt", "csv", "tsv"],
        key=StreamlitKeys.EOS_FILE_UPLOAD_WIDGET,
    )


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
    eps_values = np.logspace(eps_start, eps_end, num=200)
    p_values = polytropic_eos_p(eps_values.tolist(), kappa, gamma)
    fig, ax = plt.subplots()
    ax.set_title("Pressure vs. Energy Density")
    ax.set_xlabel("Energy Density [MeV/fm^3]")
    ax.set_xscale("log")
    ax.set_ylabel("Pressure [MeV/fm^3]")
    ax.set_yscale("log")
    ax.plot(eps_values, p_values, color="blue", label="TOV Solver")
    if tabulated_densities is not None and tabulated_pressures is not None:
        ax.scatter(
            tabulated_densities, tabulated_pressures, color="orange", label="Tabulated"
        )
    ax.legend()
    st.pyplot(fig)


# -------------------- Tabulated Equation of State --------------------


def draw_info_for_tabulated_eos():
    st.markdown("# Tabulated Equation of State")
    st.text(
        "The values used to generate the mass-radius curve are interpolated directly from a tabulated EoS file. "
    )


def draw_tabulated_eos_plot():
    fig, ax = plt.subplots()
    ax.set_title("Pressure vs. Energy Density")
    ax.set_xlabel("Energy Density [MeV/fm^3]")
    ax.set_xscale("log")
    ax.set_ylabel("Pressure [MeV/fm^3]")
    ax.set_yscale("log")
    eos_file = st.session_state[StreamlitKeys.EOS_FILE_UPLOAD_WIDGET]
    eos_data = load_eos_from_file(eos_file) if eos_file is not None else None
    if eos_data is not None:
        tabulated_densities, tabulated_pressures = eos_data
        ax.scatter(
            tabulated_densities,
            tabulated_pressures,
            color="orange",
            label="Tabulated EoS",
        )
        log_interpolator = LogarithmicInterpolator(
            x_values=tabulated_densities, y_values=tabulated_pressures
        )
        x_min = min(tabulated_densities)
        x_max = max(tabulated_densities)
        x_values = np.geomspace(x_min, x_max, num=100)
        y_values = log_interpolator.get_y(x_values)
        ax.plot(x_values, y_values, color="blue", label="Interpolated")
        ax.legend()
    _, plot_col, _ = st.columns(UiConstants.CENTERED_WITH_MARGINS_SPEC)
    with plot_col:
        st.pyplot(fig)


# -------------------- Mass-Radius Curve --------------------


def draw_central_pressure_slider():
    """
    Write the pressure range slider to the UI. Returns a tuple containing
    the chosen orders of magnitude for pressure [MeV/fm^3] in the form
    (start, end).
    """
    st.slider(
        label=r"$P$ Magnitude Range - Evaluation Range: $[10^{start}, 10^{end})$",
        # Min and max value are arbitary. Might change/remove them later.
        min_value=-20,
        max_value=20,
        value=(0, 4),
        key=StreamlitKeys.PRESSURE_SLIDER,
    )


def draw_mr_file_upload_widget():
    """
    Write the mass-radius curve file upload option to the UI. Returns a tuple of
    the form (radii, masses) if a file of the correct format was uploaded, otherwise
    None.
    """
    st.file_uploader(
        label="Choose a mass-radius data file",
        type=["txt", "csv", "tsv"],
        key=StreamlitKeys.MR_FILE_UPLOAD_WIDGET,
    )


def draw_constraint_checkboxes():
    st.markdown("### Constraints")
    st.checkbox("J0740", value=True, key=StreamlitKeys.J0740_CHECKBOX)
    st.checkbox("J0030", value=True, key=StreamlitKeys.J0030_CHECKBOX)
    st.checkbox("J0437", value=True, key=StreamlitKeys.J0437_CHECKBOX)
    st.checkbox("J0614", value=True, key=StreamlitKeys.J0614_CHECKBOX)
    st.checkbox("GW170817", value=True, key=StreamlitKeys.GW170817_CHECKBOX)


def get_constraints_from_ui() -> ObservationalConstraints:
    show_J0740 = st.session_state.get(StreamlitKeys.J0740_CHECKBOX, False)
    show_J0030 = st.session_state.get(StreamlitKeys.J0030_CHECKBOX, False)
    show_J0437 = st.session_state.get(StreamlitKeys.J0437_CHECKBOX, False)
    show_J0614 = st.session_state.get(StreamlitKeys.J0614_CHECKBOX, False)
    show_GW170817 = st.session_state.get(StreamlitKeys.GW170817_CHECKBOX, False)
    return ObservationalConstraints(
        show_J0740, show_J0030, show_J0437, show_J0614, show_GW170817
    )


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
    fig, ax = plt.subplots()
    ax.set_title("Mass-Radius Curve")
    ax.set_xlabel("Radius [km]")
    ax.set_ylabel(r"Mass [M$_\odot$]")
    ax.grid(alpha=0.3)
    if tabulated_radii is not None and tabulated_masses is not None:
        ax.scatter(tabulated_radii, tabulated_masses, color="orange", label="Tabulated")
    ax.plot(radii, masses, color="blue", label="TOV Solver")
    constraints = get_constraints_from_ui()
    plot_nicer_constraints(ax, constraints)
    plot_gw170817_constraints(ax)
    ax.set_ylim(0, 3.5)
    # TODO: Add radius-limiting slider.
    ax.set_xlim(8, 16)
    ax.legend(loc="upper left", fontsize=8)
    constraints_col, plot_col, _ = st.columns(UiConstants.CENTERED_WITH_MARGINS_SPEC)
    with constraints_col:
        draw_constraint_checkboxes()
    with plot_col:
        st.pyplot(fig)


def draw_ui_for_mass_radius_curve(eos_eps_fn: EOS_EPS_FN_TYPE, is_blank: bool = False):
    st.markdown("## Mass-Radius Curve")
    draw_central_pressure_slider()
    draw_mr_file_upload_widget()
    mr_file = st.session_state[StreamlitKeys.MR_FILE_UPLOAD_WIDGET]
    mr_data = load_mr_curve_from_file(mr_file) if mr_file is not None else None
    tabulated_radii, tabulated_masses = mr_data if mr_data is not None else (None, None)
    p_start, p_end = st.session_state[StreamlitKeys.PRESSURE_SLIDER]
    if not is_blank:
        radii, masses = generate_mass_radius_curve(
            p_c_magnitude_range=(p_start, p_end), eos_eps_fn=eos_eps_fn
        )
        draw_mass_radius_curve(radii, masses, tabulated_radii, tabulated_masses)
    else:
        draw_mass_radius_curve(
            radii=[],
            masses=[],
            tabulated_radii=tabulated_radii,
            tabulated_masses=tabulated_masses,
        )


# -------------------- General UI --------------------


def draw_and_get_eos_dropdown() -> EOS_OPTIONS_TYPE:
    """
    Write EoS selection dropdown to the UI and get the selected option.
    """
    valid_options = typing.get_args(EOS_OPTIONS_TYPE)
    # The pyright ignore statement is because Streamlit's return type isn't
    # technically correct.
    option: EOS_OPTIONS_TYPE = st.selectbox("Choose an EoS", valid_options)  # pyright: ignore[reportAssignmentType]
    return option


def draw_ui_for_polytropic_eos():
    """
    Write all components to the UI for a polytropic EoS.
    """
    draw_info_for_polytropic_eos()
    col_one, col_two = st.columns(spec=[0.4, 0.6])
    with col_one:
        draw_polytropic_parameters_inputs()
        draw_density_range_slider()
        draw_eos_file_upload_widget()
    with col_two:
        kappa = st.session_state[StreamlitKeys.POLYTROPIC_EOS_KAPPA_INPUT]
        gamma = st.session_state[StreamlitKeys.POLYTROPIC_EOS_GAMMA_INPUT]
        eps_start, eps_end = st.session_state[StreamlitKeys.ENERGY_DENSITY_SLIDER]
        eos_file = st.session_state[StreamlitKeys.EOS_FILE_UPLOAD_WIDGET]
        eos_data = load_eos_from_file(eos_file) if eos_file is not None else None
        densities, pressures = eos_data if eos_data is not None else (None, None)
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


def draw_ui_for_tabulated_eos():
    draw_info_for_tabulated_eos()
    draw_eos_file_upload_widget()
    draw_tabulated_eos_plot()
    eos_file = st.session_state[StreamlitKeys.EOS_FILE_UPLOAD_WIDGET]
    if eos_file is not None:
        eos_file.seek(0)
        eos_data = load_eos_from_file(eos_file)
        if eos_data is not None:
            densities, pressure = eos_data
            log_interpolator = LogarithmicInterpolator(
                x_values=pressure, y_values=densities
            )
            draw_ui_for_mass_radius_curve(lambda p: log_interpolator.get_y(p))
    else:
        draw_ui_for_mass_radius_curve(lambda _: 0.0, is_blank=True)


def draw_ui_for_soc_eos():
    st.text("Work In Progress")
