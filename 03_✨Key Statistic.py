import streamlit as st


df = st.session_state["df"]

st.header("Key Statistic ✨")
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
#average_latitude = int(df_selection["Latitude"].mean())
average_speed = round(df_selection["Speed"].mean(), 1)
star_rating = "😟" * int(round(average_speed, 0))

col, col2, col3 = st.columns(3)

with col:
    st.subheader("Average Speed:")
    st.subheader(f"{average_speed}")

with col2:
    st.subheader(f"{star_rating}")

#with col:
    

st.markdown("---")
    
st.bar_chart(df_selection, x="Driver", y="Event", use_container_width=True)
st.bar_chart(df_selection, x="Driver", y="Speed", use_container_width=True)
