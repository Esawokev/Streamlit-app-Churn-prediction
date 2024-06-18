import streamlit as st
import os
import base64

st.set_page_config(page_title="Multi-Page App", layout="wide")

st.sidebar.title("Navigation")
pages = {
    "Home": "home.py",
    "Data": "01_data_page.py",
    "Dashboard": "02_dashboard_page.py",
    "Prediction": "03_predict_page.py",
    "History": "04_history.py"
}
page = st.sidebar.radio("Go to", list(pages.keys()))

# Dynamically import the selected page module
page_module = __import__(f"pages.{pages[page]}", fromlist=[''])

# Call the main function of the selected page module
page_module.main()
