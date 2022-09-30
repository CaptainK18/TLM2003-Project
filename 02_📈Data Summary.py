import streamlit as st


df = st.session_state["df"]

st.header("Data Summary 📈")

st.dataframe(df.describe())