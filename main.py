import streamlit as st
import pandas as pd
import joblib

from pages import Home,Data,Dashboard,Predict,History

# Set page configuration
st.set_page_config(
    page_title='Multi-Page App',
    page_icon=':house:',
    layout='wide'
)

# Define a function to display the selected page
def main():
    st.sidebar.title("Navigation")
    pages = {
        "Home": Home,
        "01_Data":Data,
        "02_Dashboard":Dashboard,
        "03_Predict":Predict,
        "04_History":History
    }
    selection = st.sidebar.selectbox("Go to", list(pages.keys()))
    page = pages[selection]
    page.app()  # Call the app function from the selected page module

# Run the main function
if __name__ == "__main__":
    main()