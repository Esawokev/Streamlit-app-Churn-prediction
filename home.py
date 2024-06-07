import streamlit as st
import os
import base64

st.set_page_config(
    page_title='Home page',
    layout='wide',
    page_icon=':house:'
)

# Function to load an image and return the base64 encoded string
def get_base64_encoded_image(image_path):
    with open('utils/background.jpg', "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Function to set background image
def set_background_image(image_path):
    img_base64 = get_base64_encoded_image(image_path)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Apply the background image
set_background_image('utils/background.jpg')

# Example content to demonstrate the background
st.title("Customer Churn Prediction App")
#st.write("This is an example of how to set a background image in a Streamlit app.")



