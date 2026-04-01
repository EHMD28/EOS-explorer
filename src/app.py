"""
This file in the entry point of the application.
"""

from matplotlib import pyplot as plt
import numpy as np
from streamlit.cursor import T

from app_constants import EOS_DATA, MR_DATA
from plotting import generate_log_fig

import streamlit as st

from tov import generate_mr_curve


def plot_tabulated_eos():
    densities, pressures = EOS_DATA
    eos_fig = generate_log_fig(
        densities,
        pressures,
        title="Tabulated EoS",
        x_label="Energy Density [MeV/fm^3]",
        y_label="Pressure [MeV/fm^3]",
        is_scatter=True,
    )
    st.pyplot(eos_fig)


def plot_tabulated_mr():
    radii, masses = MR_DATA
    mr_fig = generate_log_fig(
        radii,
        masses,
        title="Tabulated Mass-Radius Curve",
        x_label="Radius [km]",
        y_label="Mass [M☉]",
        is_scatter=True,
    )
    mr_ax = mr_fig.axes[0]
    mr_ax.plot(radii, masses, color="orange")
    st.pyplot(mr_fig)


def plot_lin_tabulated_mr():
    radii, masses = MR_DATA
    lin_mr_fig, lin_mr_ax = plt.subplots()
    lin_mr_ax.scatter(radii, masses)
    lin_mr_ax.set_title("Linearly-Spaced Mass-Radius Curve")
    lin_mr_ax.set_xlabel("Radius [km]")
    lin_mr_ax.set_ylabel("Mass [M☉]")
    st.pyplot(lin_mr_fig)


def plot_solver_mr():
    solver_curve = generate_mr_curve(np.logspace(-15, 1).tolist())
    solver_radii, solver_masses = solver_curve
    solver_fig = generate_log_fig(solver_radii, solver_masses, is_scatter=True)
    st.pyplot(solver_fig)


def main():
    # plot_solver_mr()
    plot_tabulated_mr()
    plot_lin_tabulated_mr()
    plot_tabulated_eos()


if __name__ == "__main__":
    main()
