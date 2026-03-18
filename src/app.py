"""
This file in the entry point of the application.
"""

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import math
import streamlit as st


def f_sin(
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


def generate_plot(x_values: list[float], y_values: list[float]) -> Figure:
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    return fig


def main():
    amplitude = 1.0
    angular_frequency = 1.0
    phase = 0
    t_values, y_values = f_sin(
        amplitude, angular_frequency, phase, interval=(0, 2 * np.pi)
    )
    fig = generate_plot(t_values, y_values)
    st.pyplot(fig)


if __name__ == "__main__":
    main()
