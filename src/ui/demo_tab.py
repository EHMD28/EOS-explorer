import streamlit as st


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


def draw_ui_for_demo_tab():
    draw_dimensionless_conversion_info()
    draw_diemnsionless_conversion_inputs()
