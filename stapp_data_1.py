import streamlit as st
import numpy as np
import pandas as pd

#x = st.slider('x')  # 👈 this is a widget
#st.write(x, 'squared is', x * x)

st.number_input("Your value", key="value")

# You can access the value at any point with:
x = st.session_state.value
st.write(x, 'squared is', x * x)
