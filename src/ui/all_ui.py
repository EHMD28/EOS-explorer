from ui.main_tab import (
    draw_and_get_eos_dropdown,
    draw_ui_for_polytropic_eos,
    draw_ui_for_tabulated_eos,
)

import streamlit as st

from ui.info_tab import draw_ui_for_info_tab


def draw_ui():
    """
    Write components to user interface.
    """
    tab_names = ["Main", "Info"]
    main_tab, info_tab = st.tabs(tab_names)
    with main_tab:
        eos_dropdown = draw_and_get_eos_dropdown()
        match eos_dropdown:
            case "Polytropic":
                draw_ui_for_polytropic_eos()
            case "Tabulated":
                draw_ui_for_tabulated_eos()
    with info_tab:
        draw_ui_for_info_tab()
