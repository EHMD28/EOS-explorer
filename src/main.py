"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
from app_data import fig
import pandas as pd

st.latex(r"f(x) = \sin(x)")
st.latex(r"g(x) = \cos(x)")
st.pyplot(fig)

df = pd.DataFrame(
    {
        "y": [1, 4, 9, 16, 25],  #
    }
)
st.line_chart(df)
