"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
from app_data import fig

st.latex(r"f(x) = \sin(x)")
st.latex(r"g(x) = \cos(x)")
st.pyplot(fig)
