import streamlit as st
import pandas as pd
import base64
import os

st.set_page_config(
    page_title='History Page',
    layout='wide'
)
 

#Load an image and return the base64 encoded string
def get_base64_encoded_image(image_path):
    with open('assets/datapgbkgrnd.png', "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

#set background image
def set_background_image(image_path):
    img_base64 = get_base64_encoded_image(image_path)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Apply the background image
set_background_image('assests/datapgbkgrnd.png')

if __name__ == '__main__':
    st.title('Prediction History')
    st.write('This page displays the history of predictions made.')
    csv_path= './data/history.csv'
 
if os.path.exists(csv_path):
    history_df = pd.read_csv('./data/history.csv')
    st.dataframe(history_df)
 
else:
    st.info('Make a prediction first')
 