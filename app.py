import streamlit as st
from config import OPENWEATHER_API_KEY, GEMINI_API_KEY
from weather import get_weather
from gemini import analyze_weather

#page config
st.set_page_config(
    page_title="Weather Intelligence System",
    layout="centered"
)

#styling
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }

    h1, h2, h3 {
        color: #ffffff;
        font-weight: 600;
    }

    .card {
        background-color: #1c1f26;
        padding: 16px;
        border-radius: 10px;
        margin-bottom: 12px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        font-size: 15px;
    }

    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

#Title
st.title("Weather Intelligence System")

st.write("Enter a city to retrieve weather data and AI-based analysis.")

#Inpute
city = st.text_input("City")

analyze = st.button("Analyze")

#Logic
if analyze:

    if not city:
        st.warning("Please enter a city.")
    else:

        with st.spinner("Fetching weather data..."):
            weather_data = get_weather(city)

        if "error" in weather_data:
            st.error(weather_data["error"])
        else:

            st.markdown("### Weather Data")

            col1, col2, col3, col4 = st.columns(4)

            col1.markdown(f"<div class='card'><b>Temperature</b><br>{weather_data['temperature']} °C</div>", unsafe_allow_html=True)
            col2.markdown(f"<div class='card'><b>Feels Like</b><br>{weather_data['feels_like']} °C</div>", unsafe_allow_html=True)
            col3.markdown(f"<div class='card'><b>Humidity</b><br>{weather_data['humidity']}%</div>", unsafe_allow_html=True)
            col4.markdown(f"<div class='card'><b>Wind Speed</b><br>{weather_data['wind_speed']} m/s</div>", unsafe_allow_html=True)

            st.markdown("### AI Analysis")

            with st.spinner("Processing..."):
                analysis = analyze_weather(weather_data)

            st.markdown(f"""
            <div class="card">
            {analysis}
            </div>
            """, unsafe_allow_html=True)