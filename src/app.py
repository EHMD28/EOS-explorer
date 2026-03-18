"""
This file in the entry point of the application.
"""

import streamlit as st
from app_data import fig
import pandas as pd
import numpy as np


def f(x):
    return x**2


def main():
    st.latex(r"f(x) = \sin(x)")
    st.latex(r"g(x) = \cos(x)")
    st.pyplot(fig)

    x_values = np.linspace(0, 20)
    y_values = np.sin(x_values)
    df = pd.DataFrame(
        {
            "y": y_values,  #
        }
    )
    st.text("Hello, World")
    st.line_chart(df)


if __name__ == "__main__":
    main()
