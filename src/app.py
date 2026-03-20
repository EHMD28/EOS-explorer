"""
This file in the entry point of the application.
"""

from typing import Literal

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import math
import streamlit as st


def get_sin_wave_points(
    amplitude: float,
    angular_frequency: float,
    phase: float,
    interval: tuple[float, float],
) -> tuple[list[float], list[float]]:
    start, end = interval
    t_values = np.linspace(start, end, num=200)
    A = amplitude
    omega = angular_frequency
    phi = phase
    y_values = [A * math.sin(omega * t - phi) for t in t_values]
    return (t_values.tolist(), y_values)


def get_baseline_sin_wave_points(
    interval: tuple[float, float],
) -> tuple[list[float], list[float]]:
    start, end = interval
    t_values, y_values = get_sin_wave_points(
        amplitude=1.0, angular_frequency=1.0, phase=0, interval=(start, end)
    )
    return (t_values, y_values)


def generate_sin_plot(
    t_values: list[float],
    y_values: list[float],
    interval: tuple[float, float],
    show_baseline: bool = True,
) -> Figure:
    fig, ax = plt.subplots()
    if show_baseline:
        b_xs, b_ys = get_baseline_sin_wave_points(interval)
        ax.plot(b_xs, b_ys, color="blue", label="Baseline")
    ax.plot(t_values, y_values, color="red")
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    ax.legend()
    fig.tight_layout()
    return fig


def get_sine_wave_figure_with_parameters():
    amplitude = st.slider("A", value=1)
    angular_frequency = st.slider("ω", value=1)
    phase = st.slider("φ", value=0)
    st.write(amplitude, angular_frequency, phase)
    start = 0
    end = 2 * np.pi
    t_values, y_values = get_sin_wave_points(
        amplitude, angular_frequency, phase, interval=(0, 2 * np.pi)
    )
    fig = generate_sin_plot(
        t_values,
        y_values,
        interval=(start, end),
        show_baseline=st.checkbox("Show Baseline"),
    )
    return fig


def main():
    option: Literal["sine wave", "parabola"] = st.selectbox(
        label="Choose an option", options=["sine wave", "parabola"]
    )
    fig = None
    if option == "sine wave":
        fig = get_sine_wave_figure_with_parameters()
    elif option == "parabola":
        ...
    st.pyplot(fig)


if __name__ == "__main__":
    main()
