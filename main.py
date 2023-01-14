import streamlit as st
import plotly.express as px
from data_function import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky Conditions"))
if place:
    if days > 1:
        st.subheader(f"{option} for the next {days} days in {place}")
    else:
        st.subheader(f"{option} for the next day in {place}")

    d, t = get_data(days)

    figure = px.line(x=d, y=t, labels={"x": "Date", "y":"Temperature (C)"})
    st.plotly_chart(figure)
