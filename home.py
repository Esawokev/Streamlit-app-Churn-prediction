import streamlit as st
import os
import base64

st.set_page_config(
    page_title='Home page',
    layout='wide',
    page_icon=':house:'
)

#Load an image and return the base64 encoded string
def get_base64_encoded_image(image_path):
    with open('utils/background.jpg', "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

#set background image
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

# Page title
st.title("Customer Churn Prediction App")

# Tagline

st.markdown("<p style='color:black; font-style:italic;font-weight:bold;'>Helping you retain your business lifeline through customer management...</p>", unsafe_allow_html=True)

# Sidebar for contact information
st.sidebar.title("Contact Information")
st.sidebar.markdown("<i class='fas fa-phone'></i> Phone: +2547000111", unsafe_allow_html=True)
st.sidebar.markdown("<i class='fas fa-envelope'></i> Email: systems@cmmanagement.com", unsafe_allow_html=True)
st.sidebar.markdown("<i class='fas fa-map-marker-alt'></i> Address: 1023 Moi Avenue, Nairobi, Kenya", unsafe_allow_html=True)



