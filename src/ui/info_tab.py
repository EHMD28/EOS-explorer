import textwrap

import streamlit as st


def draw_ui_for_info_tab():
    text = textwrap.dedent("""\
    # Eos Explorer 

    Eos Explorer is an interactive application which allows the user to programatically study the equation of state of neutron-star matter. The full source code is available on [Github](https://github.com/EHMD28/EOS-explorer).

    ## File Uploading

    The application automatically infers to delimeter of any data files based on the file extension.

    - `txt`: Spaces
    - `csv`: Commas
    - `tsv`: Tabs
    """)
    st.markdown(text)
