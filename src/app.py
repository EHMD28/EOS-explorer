"""
This file in the entry point of the application.
"""

from typing import Literal

import streamlit as st

from functions.parabola import get_parabola_figure_with_parmaters, show_parabola_info
from functions.sine_wave import get_sine_wave_figure_with_parameters, show_sine_wave_info


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
