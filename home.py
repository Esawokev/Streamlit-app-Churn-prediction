import streamlit as st
import os

st.set_page_config(
    page_title='Home page',
    layout='wide',
    page_icon=':house:'
)

# Define custom CSS to set the background image
def set_background_image():
    # Get the absolute path of the directory containing the script
    current_dir = os.path.dirname(os.path.abspath("C:/Users/lucky/Desktop/LP4/Streamlit-Model-deployment/Streamlit-app-Churn-prediction/Utils/background.jpg"))
    # Construct the path to the background image
    background_img_path = os.path.join(current_dir, 'utils', 'background.jpg')

    # Define the CSS with the absolute path to the image
    page_bg_img = f"""
    <style>
    .stApp {{
        background: url("C:/Users/lucky/Desktop/LP4/Streamlit-Model-deployment/Streamlit-app-Churn-prediction/Utils/background.jpg"") no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """

    # Inject the custom CSS into the Streamlit app
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Apply the background image
set_background_image()

# Example content to demonstrate the background
st.title("Customer Churn Prediction App")
st.write("This is an example of how to set a background image in a Streamlit app.")

