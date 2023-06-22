import streamlit as st
import plotly.express as px
from backend import get_data



# Add title, text input, slider, selection, and subheader widget
st.title("Weather Forcat for Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days",
                 min_value=1,
                 max_value=5,
                 help="Select the number of forecastes days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


if place:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # Create a temperature plot
            #temperature = [dict["main"]["temp"] for dict in filtered_data]
            ## ardit solution
            temperature = [dict["main"]["temp"] / 10 for dict in filtered_data]
            ## display in celsius my soulution
            ## celsius = [round(temp/10, 2) for temp in temperature]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperature, labels={
                            "x": "Date", "y": "Temprature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png",
            "Clouds" : "images/cloud.png",
            "Rain" : "images/rain.png",
            "Snow" : "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=80)
    except KeyError:
        st.info("That place does not exist!")


