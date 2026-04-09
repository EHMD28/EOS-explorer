"""
This file in the entry point of the application.
"""

import streamlit as st

from app_constants import AppConstants
from ui.all_ui import draw_ui


def configure_streamlit():
    st.set_page_config(
        page_title="EoS Explorer", page_icon=AppConstants.FAVICON_PATH, layout="wide"
    )


def main():
    configure_streamlit()
    draw_ui()


if __name__ == "__main__":
    main()
