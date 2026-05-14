import streamlit as st

from app_constants import EosConstants
from solver import solve_dimensionless_tov
from eos.polytropic import eos_eps as polytropic_eos_eps


def draw_tov_equations_info():
    st.markdown("### Different Forms of the TOV Equation")
    st.latex(
        r"\frac{\mathrm{d} P(r)}{\mathrm{d} r} = \frac{-G m_r(r) \rho(r)}{r^2} \left(1 + \frac{P(r)}{\rho c^2} \right) \left(1 + \frac{4\pi r^3 P(r)}{m_r(r) c^2} \right) \left(1 - \frac{2 G m_r(r)}{r c^2} \right)^{-1}"
    )
    st.markdown("General TOV Equation", text_alignment="center")
    st.latex(
        r"\frac{\mathrm{d} P(r)}{\mathrm{d} r} = -\frac{G m_r(r) \varepsilon(r)}{r^2} \left(1 + \frac{P(r)}{\varepsilon(r)} \right) \left(1 + \frac{4\pi r^3 P(r)}{m_r(r)} \right) \left(1 - \frac{2 G m_r(r)}{r} \right)^{-1}"
    )
    st.markdown("Relativistic TOV Equation ($c = 1$)", text_alignment="center")
    st.latex(
        r"\frac{\mathrm{d} P'}{\mathrm{d} r'} =  -\frac{m_r' \cdot \varepsilon'}{r'^2} \left(1 + \frac{P'}{\varepsilon'} \right) \left(1 + \frac{4\pi \cdot r'^3 \cdot P'}{m_r'} \right) \left(1 - \frac{2 m_r'}{r'} \right)^{-1}"
    )
    st.markdown("Dimensionless Relativistic TOV Equation", text_alignment="center")


def draw_relativistic_equations_info():
    st.latex(
        r"c = \frac{3.0 \times 10^8 \space \mathrm{meters}}{1 \space \mathrm{second}}"
    )
    st.latex(r"c = 1")
    st.latex(
        r"\frac{3.0 \times 10^8 \space \mathrm{meters}}{1 \space \mathrm{second}} = 1"
    )
    st.latex(r"3.0 \times 10^8 \space \mathrm{meters} = 1 \space \mathrm{second}")
    st.latex(
        r"1 \space \mathrm{meters} = \frac{1}{3.0 \times 10^8} \space \mathrm{seconds}"
    )


def draw_dimensionless_conversion_info():
    st.markdown("### Dimensionless Scaling Equations")
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.latex(r"P = P' \cdot \varepsilon_0")
    with col2:
        st.latex(r"\varepsilon = \varepsilon' \cdot \varepsilon_0")
    with col3:
        st.latex(r"r = \frac{r'}{\sqrt{G \cdot \varepsilon_0}}")
    with col4:
        st.latex(r"m_r = \frac{m_r'}{\sqrt{G^3 \cdot \varepsilon_0}}")
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.latex(r"P' = \frac{P}{\varepsilon_0}")
    with col2:
        st.latex(r"\varepsilon' = \frac{\varepsilon}{\varepsilon_0}")
    with col3:
        st.latex(r"r' = r \sqrt{G \cdot \varepsilon_0}")
    with col4:
        st.latex(r"m_r' = m_r \sqrt{G^3 \cdot \varepsilon_0}")


def draw_pressure_energy_density_scaling_col(eps_0: float):
    p = st.number_input(
        r"$P$ or $\varepsilon$ - Pressure or Energy Density [MeV/fm^3]", value=150.0
    )
    p_p = p / eps_0
    st.markdown(f"Pressure or Energy Density [dimensionless] = {p_p}")
    p_p = st.number_input(
        r"$P'$ or $\varepsilon'$- Pressure or Energy Density [dimensionless]", value=1.5
    )
    p = p_p * eps_0
    st.text(f"Pressure or Energy Density [MeV/fm^3] = {p}")


def draw_radius_scaling_col():
    st.number_input("$r$ - Radius [km]")
    st.text("Radius [dimensionless] = 0.0")
    st.number_input("$r'$ - Radius [dimensionless]")
    st.text("Radius [km] = 0.0")


def draw_mass_scaling_col():
    st.number_input(r"$m_r$ - Mass [M$_\odot$]")
    st.text("Mass [dimensionless] = 0.0")
    st.number_input("$m_r'$ - Mass [dimensionless]")
    st.markdown(r"Mass [M$_\odot$] = 0.0")


def draw_diemnsionless_conversion_inputs():
    eps_0 = st.number_input(r"$\varepsilon_0$ - Scaling Constant [MeV/fm^3]", value=100)
    draw_pressure_energy_density_scaling_col(eps_0)


def draw_ui_for_single_star_with_polytrope():
    st.markdown("### Single Star Solver")
    kappa = st.number_input(
        "K - Constant of Proportionality",
        value=EosConstants.DEFAULT_KAPPA,
        format="%.4e",
    )
    gamma = st.number_input(
        r"$\gamma$ - Polytropic Exponent",
        value=EosConstants.DEFAULT_GAMMA,
        format="%.4f",
    )
    p_c = st.number_input("$p_c$ - Central Pressure [MeV/fm^3]", value=150)
    r, m = solve_dimensionless_tov(p_c, lambda p: polytropic_eos_eps(p, kappa, gamma))
    st.markdown(f"Radius: {r} km")
    st.markdown(f"Mass: {m} M$_\\odot$")


def draw_ui_for_demo_tab():
    draw_tov_equations_info()
    st.divider()
    draw_relativistic_equations_info()
    st.divider()
    draw_dimensionless_conversion_info()
    draw_diemnsionless_conversion_inputs()
    st.divider()
    draw_ui_for_single_star_with_polytrope()
