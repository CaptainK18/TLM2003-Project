import streamlit as st


df = st.session_state["df"]

st.header("Data Sheet 📊")

st.dataframe(df)