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
user_input = {
    'gender': st.selectbox('Gender', options=['Male', 'Female'], key='gender'),
    'marital_status': st.selectbox('Marital Status', options=['Single', 'Married'], key='marital_status'),
    'dependents': st.number_input('Dependents', min_value=0, max_value=10, key='dependents'),
    'internetservice': st.selectbox('Internet Service', options=['DSL', 'Fiber optic', 'No'], key='internetservice'),
    'contract': st.selectbox('Contract', options=['Month-to-month', 'One year', 'Two year'], key='contract'),
    'tenure': st.number_input('Tenure (months)', min_value=0, key='tenure'),
    'paymentmethod': st.selectbox('Payment Method', options=['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], key='payment_method'),
    'monthlycharges': st.number_input('Monthly Charges', min_value=0.0, key='monthly_charges'),
    'totalcharges': st.number_input('Total Charges', min_value=0.0, key='total_charges'),
    'seniorcitizen': st.selectbox('Senior Citizen', options=['Yes', 'No'], key='seniorcitizen'),
    'paperlessbilling': st.selectbox('Paperless Billing', options=['Yes', 'No'], key='paperlessbilling'),
    'multiplelines': st.selectbox('Multiple Lines', options=['Yes', 'No', 'No phone service'], key='multiplelines'),
    'onlinesecurity': st.selectbox('Online Security', options=['Yes', 'No', 'No internet service'], key='onlinesecurity'),
    'phoneservice': st.selectbox('Phone Service', options=['Yes', 'No'], key='phoneservice'),
    'deviceprotection': st.selectbox('Device Protection', options=['Yes', 'No', 'No internet service'], key='deviceprotection'),
    'techsupport': st.selectbox('Tech Support', options=['Yes', 'No', 'No internet service'], key='techsupport'),
    'streamingtv': st.selectbox('Streaming TV', options=['Yes', 'No', 'No internet service'], key='streamingtv'),
    'streamingmovies': st.selectbox('Streaming Movies', options=['Yes', 'No', 'No internet service'], key='streamingmovies'),
    'onlinebackup': st.selectbox('Online Backup', options=['Yes', 'No', 'No internet service'], key='onlinebackup')
}
# Create DataFrame from session state
user_input = {key: st.session_state[key] for key in st.session_state.keys()}
df = pd.DataFrame([user_input])


#create a form
def display_form():
    col1, col2= st.columns(2)
    with col1:
        selected_dashboard = st.selectbox('Select the type of Dashboard', options=['EDA', 'KPIs'], key='selected_dashboard_type')
    
    

    with st.form('input_features'):
        st.write('### Family Information')
        with st.expander("Customer Info"):
            col1, col2 = st.columns(2)
            with col1:
                st.selectbox('Senior Citizen', options=[('No'), ('Yes')], key='seniorcitizen')
                st.selectbox('Gender', options=['Male', 'Female'], key='gender')
                st.selectbox('Partner', options=['Yes', 'No'], key='marital_status')
                st.selectbox('Dependents', options=['Yes', 'No'], key='dependents')

        st.write('### Product Profile')
        with st.expander("Product Profile"):
            col1, col2 = st.columns(2)
            with col1:
                st.selectbox('What is your internet service?', options=['DSL', 'Fiber optics'], key='internetservice')
                st.selectbox('Select your contract type', options=['Month-to-month', 'One year', 'Two year'], key='contract')
                st.selectbox('What is your mode of payment?', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], key='payment_method')
            with col2:
                st.number_input('What are your monthly charges?', key='monthly_charges', min_value=18.34, max_value=118.65,step=10.00)
                st.number_input('What are the total charges?', key='total_charges', min_value=18.80, max_value=8670.10,step=100.00)
                st.number_input('How many months have you been a client?', key='tenure', min_value=0, max_value=72, step=6)

        st.write('### Additional Services')
        with st.expander("Additional Services"):
            col1, col2 = st.columns(2)
            with col1:
                st.selectbox('Paperless Billing', options=['Yes', 'No'], key='paperlessbilling')
                st.selectbox('Phone Service', options=['Yes', 'No'], key='phoneservice')
                st.selectbox('Multiple Lines', options=['Yes', 'No'], key='multiplelines')
                st.selectbox('Device Protection', options=['Yes', 'No'], key='deviceprotection')
            with col2:
                st.selectbox('Online Security', options=['Yes', 'No'], key='onlinesecurity')
                st.selectbox('Online Backup', options=['Yes', 'No'], key='onlinebackup')
                
                st.selectbox('Tech Support', options=['Yes', 'No'], key='techsupport')
                st.selectbox('Streaming TV', options=['Yes', 'No'], key='streamingtv')
                st.selectbox('Streaming Movies', options=['Yes', 'No'], key='streamingmovies')
                

        st.form_submit_button('Submit')
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Data submitted successfully!")

    # Update session state
    for key in st.session_state.keys():
        if key in user_input:
            user_input[key] = st.session_state[key]


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
