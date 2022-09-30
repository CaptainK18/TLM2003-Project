import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

df = st.session_state["df"]

st.header("Map Data 🗺️")

vehicle = st.sidebar.multiselect(
    "Select the Vehicle:", 
    options = df["Vehicle"].unique(),
    default = df["Vehicle"].unique()
)   
driver = st.sidebar.multiselect(
    "Select the Driver:", 
    options = df["Driver"].unique(),
    default = df["Driver"].unique()
)  
df_selection = df.query(
    "Vehicle == @vehicle & Driver == @driver"
)

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=1.290270,
        longitude=103.851959,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=df_selection,
           get_position='[Longitude, Latitude]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df_selection,
            get_position='[Longitude, Latitude]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ], 
))

st.dataframe(df_selection)