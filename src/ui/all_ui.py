from ui.debugging_tab import draw_ui_for_dimensionless_conversion
from ui.eos_tab import (
    draw_and_get_eos_dropdown,
    draw_ui_for_polytropic_eos,
    draw_ui_for_soc_eos,
    draw_ui_for_tabulated_eos,
)

import streamlit as st


def draw_ui():
    """
    Write components to user interface.
    """
    tab_names = ["Main", "Debugging"]
    main_tab, debug_tab = st.tabs(tab_names)
    with main_tab:
        eos_dropdown = draw_and_get_eos_dropdown()
        match eos_dropdown:
            case "Polytropic":
                draw_ui_for_polytropic_eos()
            case "Tabulated":
                draw_ui_for_tabulated_eos()
            case "Speed-of-Sound Interpolation":
                draw_ui_for_soc_eos()
    with debug_tab:
        draw_ui_for_dimensionless_conversion()
