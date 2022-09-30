import string
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title = 'Bus Route Data Explorer', layout = "wide", page_icon = ":bus:")

df = pd.read_csv("juneroute.csv")                    # Read a CSV file 
st.session_state["df"] = df

# Add a title and intro text
st.title(":bus: Bus Route Smart Dashboard")
st.text("This is a web app to allow exploration of Bus Route Data")

image = Image.open('Image/Bus 1.jpg')
st.image(image, width=500)





