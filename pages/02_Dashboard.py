import streamlit as st
import os
import base64
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title='Dashboard Page',
    layout='wide',
    page_icon=':dashboard:'
)

# Load an image and return the base64 encoded string
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set background image
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
set_background_image('utils/dashboardbkgrnd.jpg')

# Page title
def main():
    st.title("Dashboard Page")

    

# User input
df = pd.read_csv('./data/clean_data.csv')


# EDA Dashboard
def eda_dashboard():
    st.markdown('### Exploratory Data Analysis')

    # EDA options
    eda_option = st.selectbox('Choose EDA Visualization', options=['Summary Statistics', 'Correlation Matrix', 'Scatter Plot', 'Histogram', 'Box Plot'])

    if eda_option == 'Summary Statistics':
        st.write(df.describe())

    elif eda_option == 'Correlation Matrix':
        corr_matrix = df.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr_matrix, annot=True, ax=ax)
        st.pyplot(fig)

    elif eda_option == 'Scatter Plot':
        x_axis = st.selectbox('X-axis', options=df.columns)
        y_axis = st.selectbox('Y-axis', options=df.columns)
        scatter_plot = px.scatter(df, x=x_axis, y=y_axis, title=f'Scatter Plot: {x_axis} vs {y_axis}')
        st.plotly_chart(scatter_plot)

    elif eda_option == 'Histogram':
        column = st.selectbox('Column', options=df.columns)
        histogram = px.histogram(df, x=column, title=f'Histogram of {column}')
        st.plotly_chart(histogram)

    elif eda_option == 'Box Plot':
        column = st.selectbox('Column', options=df.columns)
        box_plot = px.box(df, y=column, title=f'Box Plot of {column}')
        st.plotly_chart(box_plot)

# KPI Dashboard
def kpi_dashboard():
    st.markdown('### Key Performance Index')
    
    # Example KPIs
    st.write('**Total Charges**:', df['totalcharges'].sum())
    st.write('**Average Monthly Charges**:', df['monthlycharges'].mean())
    st.write('**Average Tenure**:', df['tenure'].mean())

# Main
if __name__ == "__main__":
    col1, col2 = st.columns(2)
    with col1:
        pass
    with col2:
        st.selectbox('Select the type of Dashboard', options=['EDA', 'KPIs'], key='selected_dashboard_type')
    
    if st.session_state['selected_dashboard_type'] == 'EDA':
        eda_dashboard()
    else:
        kpi_dashboard()
