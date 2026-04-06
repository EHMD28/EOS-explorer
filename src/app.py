"""
This file in the entry point of the application.
"""

from app_constants import AppConstants

import streamlit as st

from ui import draw_ui


def configure_streamlit():
    st.set_page_config(
        page_title="EOS Explorer", page_icon=AppConstants.FAVICON_PATH, layout="wide"
    )


def main():
    configure_streamlit()
    draw_ui()
    # plot_tabulated_mr()
    # plot_lin_tabulated_mr()
    # plot_tabulated_eos()
    # plot_lin_tabulated_eos()


if __name__ == "__main__":
    main()
