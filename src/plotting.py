"""
Utility functions for figure generation.
"""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def generate_lin_fig(
    xs: list[float],
    ys: list[float],
    title: str = "",
    x_label: str = "",
    y_label: str = "",
    is_scatter: bool = False,
) -> Figure:
    """
    Generate a figure with linear axes. `xs` and `ys` are the x-values and
    y-values of the data respsectively. The rest of the arguments are pretty
    self-explanatory.
    """
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if is_scatter:
        ax.scatter(xs, ys)
    else:
        ax.plot(xs, ys)
    fig.add_axes(ax)
    return fig


def generate_log_fig(
    xs: list[float],
    ys: list[float],
    title: str = "",
    x_label: str = "",
    y_label: str = "",
    is_scatter: bool = False,
) -> Figure:
    """
    Generate a figure with logarithmic axes. `xs` and `ys` are the x-values and
    y-values of the data respsectively. The rest of the arguments are pretty
    self-explanatory.
    """
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xscale("log")
    ax.set_yscale("log")
    if is_scatter:
        ax.scatter(xs, ys)
    else:
        ax.plot(xs, ys)
    fig.add_axes(ax)
    return fig
