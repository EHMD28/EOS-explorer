"""
This file in the entry point of the application.
"""

from cycler import cycler
import matplotlib
import streamlit as st

from app_constants import AppConstants
from ui.all_ui import draw_ui


def configure_app():
    st.set_page_config(
        page_title="EoS Explorer", page_icon=AppConstants.FAVICON_PATH, layout="wide"
    )
    # Configure the default color cycle for Matplotlib so the colors don't
    # accidentally overlap.
    matplotlib.rcParams["axes.prop_cycle"] = cycler(
        color=[
            "orange",  # I think orange constrasts best with blue.
            "red",
            "green",
            "indigo",
            "violet",
            "gray",
            "brown",
            "black",
        ]
    )


def main():
    configure_app()
    draw_ui()


if __name__ == "__main__":
    main()
