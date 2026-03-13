"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0, 2 * np.pi, 100)
sin_y_values = np.sin(x_values)
cos_y_values = np.cos(x_values)
fig, ax = plt.subplots()

ax.plot(x_values, sin_y_values, color="red")
ax.plot(x_values, cos_y_values, color="blue")
ax.axhline(y=0, linestyle="--")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.tight_layout()

st.markdown(":red[f(x) = sin x]")
st.markdown(":blue[f(x) = cos x]")
st.pyplot(fig)
