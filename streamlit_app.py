import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="ViBe - Educational Platform",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:3141")

st.title("ViBe - Adaptive Learning Platform")
st.markdown("Enhance your learning through continuous assessment and interactive challenges.")

# Add your UI components here
# Example:
if st.button("Get Courses"):
    try:
        response = requests.get(f"{API_BASE_URL}/courses")
        if response.status_code == 200:
            st.success("Connected to backend!")
            st.json(response.json())
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")

st.markdown("---")
st.markdown("*Powered by ViBe - Continuous Active Learning*")