import streamlit as st

from app_constants import ScalingConstants, StreamlitKeys
from tov.dimensionless import pressure_prime


def draw_ui_for_pressure_density_conversion():
    st.markdown("## Pressure and Energy Density")
    p_nu = st.number_input(
        "Pressure or Energy Density [MeV/fm^3]",
        value=1.0,
        format="%0.10f",
        key=StreamlitKeys.PRESSURE_NU_INPUT,
    )
    p_prime_init_val: float = pressure_prime(p_nu)  # pyright: ignore[reportAssignmentType]
    p_prime = st.number_input(
        "Pressure of Energy Density [dimensionless]",
        value=p_prime_init_val,
        format="%0.10f",
        key=StreamlitKeys.PRESSURE_PRIME_INPUT,
    )


def draw_ui_for_dimensionless_conversion():
    st.markdown("# Dimensionless Value Conversions")
    st.markdown(f"Arbitrary Scaling Constant: {ScalingConstants.EPS_0} M_sun/km^3")
    draw_ui_for_pressure_density_conversion()
