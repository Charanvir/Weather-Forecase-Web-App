import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
if place:
    if days > 1:
        st.subheader(f"{option} for the next {days} days in {place}")
    else:
        st.subheader(f"{option} for tomorrow in {place}")

    try:
        data = get_data(place, days)

        if option == "Temperature":
            filtered_data = [temp_dict["main"]["temp"] for temp_dict in data]
            temperature = [temp-273.15 for temp in filtered_data]
            dates = [date_dict["dt_txt"] for date_dict in data]
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [sky_dict["weather"][0]["main"] for sky_dict in data]
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            file_paths = [images[condition] for condition in sky_conditions]
            st.image(file_paths, width=85)

    except KeyError:
        st.subheader("Please enter a valid city name to get forecast data")
