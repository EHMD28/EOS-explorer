"""
This file in the entry point of the application.
"""

from typing import Literal

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import math
import streamlit as st


def show_sine_wave_info():
    st.latex(r"y(t) = A \sin(\omega t - \phi)")
    st.markdown(r"$A$ = ampltidue")
    st.markdown(r"$\omega$ = angular frequency")
    st.markdown(r"$\phi$ = phase shift")
    st.markdown(
        r"The baseline sine wave function is $y(t) = \sin(t)$. See [this page](https://en.wikipedia.org/wiki/Sine_wave) for more information."
    )


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


@st.cache_data
def get_baseline_sin_wave_points(
    interval: tuple[float, float],
) -> tuple[list[float], list[float]]:
    return get_sin_wave_points(
        amplitude=1.0, angular_frequency=1.0, phase=0, interval=interval
    )


def get_sin_plot(
    t_values: list[float],
    y_values: list[float],
    interval: tuple[float, float],
    show_baseline: bool = True,
) -> Figure:
    fig, ax = plt.subplots()
    if show_baseline:
        b_xs, b_ys = get_baseline_sin_wave_points(interval)
        ax.plot(b_xs, b_ys, color="blue", label="Baseline")
    ax.plot(t_values, y_values, color="red", label="_with_parameters")
    ax.set_title("Sine Wave")
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
    start = st.number_input(label="Interval Start", value=0.0, format="%0.5f")
    end = st.number_input(label="Interval End", value=2 * np.pi, format="%0.5f")
    interval = (start, end)
    t_values, y_values = get_sin_wave_points(
        amplitude, angular_frequency, phase, interval
    )
    fig = get_sin_plot(
        t_values,
        y_values,
        interval,
        show_baseline=st.checkbox("Show Baseline", value=True),
    )
    return fig


def show_parabola_info():
    st.latex(r"y = ax^2 + bx + c")
    st.markdown("The baseline parabola function is $y = x^2$")


def get_parabola_points(
    a: float, b: float, c: float, interval: tuple[float, float]
) -> tuple[list[float], list[float]]:
    start, end = interval
    points = np.linspace(start, end, 200)
    y_values = [a * x**2 + b * x + c for x in points]
    return (points.tolist(), y_values)


@st.cache_data
def get_baseline_parabola_points(interval: tuple[float, float]):
    return get_parabola_points(a=1, b=0, c=0, interval=interval)


def get_parabola_plot(
    x_values: list[float],
    y_values: list[float],
    interval: tuple[float, float],
    show_baseline: bool,
) -> Figure:
    fig, ax = plt.subplots()
    if show_baseline:
        b_xs, b_ys = get_baseline_parabola_points(interval)
        ax.plot(b_xs, b_ys, color="blue")
    ax.plot(x_values, y_values, color="red")
    ax.set_title("Parabola")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    return fig


def get_parabola_figure_with_parmaters():
    a = st.slider("a", value=1)
    b = st.slider("b")
    c = st.slider("c")
    start = st.number_input(label="Interval Start", value=-10.0, format="%0.5f")
    end = st.number_input(label="Interval End", value=10.0, format="%0.5f")
    interval = (start, end)
    x_values, y_values = get_parabola_points(a, b, c, interval)
    fig = get_parabola_plot(
        x_values,
        y_values,
        interval,
        show_baseline=st.checkbox("Show Baseline", value=True),
    )
    return fig


def main():
    option: Literal["sine wave", "parabola"] = st.selectbox(
        label="Choose an option", options=["sine wave", "parabola"]
    )
    fig = None
    if option == "sine wave":
        show_sine_wave_info()
        fig = get_sine_wave_figure_with_parameters()
    elif option == "parabola":
        show_parabola_info()
        fig = get_parabola_figure_with_parmaters()
    st.pyplot(fig)


if __name__ == "__main__":
    main()
