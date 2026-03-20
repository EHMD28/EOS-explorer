import streamlit as st
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


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
        ax.plot(b_xs, b_ys, color="blue", label="Baseline")
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
