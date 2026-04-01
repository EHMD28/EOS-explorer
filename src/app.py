"""
This file in the entry point of the application.
"""

import numpy as np

from app_constants import EOS_DATA, MR_DATA
from plotting import generate_log_fig

import streamlit as st

from tov import generate_mr_curve


def main():
    densities, pressures = EOS_DATA
    eos_fig = generate_log_fig(densities, pressures, is_scatter=True)
    radii, masses = MR_DATA
    mr_fig = generate_log_fig(radii, masses, is_scatter=True)
    solver_curve = generate_mr_curve(np.logspace(-10, -1).tolist())
    solver_radii, solver_masses = solver_curve
    solver_fig = generate_log_fig(solver_radii, solver_masses, is_scatter=True)
    st.pyplot(eos_fig)
    st.pyplot(mr_fig)
    st.pyplot(solver_fig)


if __name__ == "__main__":
    main()
