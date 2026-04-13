from matplotlib import pyplot as plt
import streamlit as st

from app_constants import DebugConstants, ScalingConstants, StreamlitKeys
from tov.dimensionless import pressure_nu, pressure_prime
from tov.solver import TOV_Solutions, solve_dimensionless_tov
from eos.polytropic import eos_eps as polytropic_eos_eps


def handle_pressue_nu_change():
    p_nu: float = st.session_state[StreamlitKeys.PRESSURE_NU_INPUT]
    p_p = pressure_prime(p_nu)
    st.session_state[StreamlitKeys.PRESSURE_PRIME_OUTPUT] = p_p


def handle_pressure_prime_change():
    p_p: float = st.session_state[StreamlitKeys.PRESSURE_PRIME_INPUT]
    p_nu = pressure_nu(p_p)
    st.session_state[StreamlitKeys.PRESSURE_NU_OUTPUT] = p_nu


def draw_dimensionless_conversion_info():
    st.markdown("# Dimensionless Value Conversions")
    st.markdown(
        f"Arbitrary Scaling Constant ($\\varepsilon_0$): {ScalingConstants.EPS_0} MeV/fm^3"
    )
    st.latex(r"P = \varepsilon_0 \cdot P'")
    st.latex(r"\varepsilon = \varepsilon_0 \cdot \varepsilon'")


def draw_ui_for_pressure_density_conversion():
    st.markdown("## Pressure and Energy Density")
    st.number_input(
        "Pressure or Energy Density [MeV/fm^3]",
        value=100.0,
        format="%e",
        key=StreamlitKeys.PRESSURE_NU_INPUT,
        on_change=handle_pressue_nu_change,
    )
    p_eps_p = st.session_state.get(StreamlitKeys.PRESSURE_PRIME_OUTPUT, 1.0)
    st.text(f"Pressure or Energy Density [dimensionless]: {p_eps_p:e}")
    st.number_input(
        "Pressure or Energy Density [dimensionless]",
        value=1.0,
        format="%e",
        key=StreamlitKeys.PRESSURE_PRIME_INPUT,
        on_change=handle_pressure_prime_change,
    )
    p_eps_nu = st.session_state.get(StreamlitKeys.PRESSURE_NU_OUTPUT, 100.0)
    st.text(f"Pressure or Energy Density [MeV/fm^3]: {p_eps_nu:e}")


def draw_solver_fig(solutions: TOV_Solutions):
    st.text(f"Total Radius: {solutions.total_radius} km")
    st.text(f"Total Mass: {solutions.total_mass} M_sun")
    # TODO: Move to plotting.py
    # fig, ax = plt.subplots()
    # ax.plot(
    #     solutions.solver_df["r_prime"],
    #     solutions.solver_df["p_prime"],
    #     color="red",
    #     label="Pressure",
    # )
    # ax.plot(
    #     solutions.solver_df["r_prime"],
    #     solutions.solver_df["m_prime"],
    #     color="blue",
    #     label="Mass",
    # )
    # ax.legend()
    # ax.set_xscale("log")
    # ax.set_yscale("log")
    # st.pyplot(fig)


def draw_ui_for_tov_solver():
    st.markdown("## TOV Solver")
    p_c = st.number_input("Central Pressure [MeV/fm^3]", value=150, format="%e")
    radius_km, mass_msun = solve_dimensionless_tov(
        p_c,
        eos_eps_nu_fn=lambda p: polytropic_eos_eps(
            p,
            kappa=DebugConstants.MID_DENSITY_KAPPA,
            gamma=DebugConstants.MID_DENSITY_GAMMA,
        ),  #
    )  # TODO: Change this
    st.text(f"Radius: {radius_km} km")
    st.text(f"Mass: {mass_msun} M_sun")


def draw_ui_for_dimensionless_conversion():
    draw_dimensionless_conversion_info()
    draw_ui_for_pressure_density_conversion()
    draw_ui_for_tov_solver()
