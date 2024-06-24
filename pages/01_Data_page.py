import streamlit as st
import pyodbc
import pandas as pd
import base64
 
st.set_page_config(
    page_title='Data Page',
    layout='wide'
)
 

#Load an image and return the base64 encoded string
def get_base64_encoded_image(image_path):
    with open('utils/predbkgrnd.png', "rb") as img_file:
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
set_background_image('utils/predbkgrnd.png')

st.title('Telco Customer Churn Database')
 
@st.cache_resource(show_spinner='connecting to database...')
def init_connection():
    return pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + st.secrets['SERVER']
        + ";DATABASE="
        + st.secrets['DATABASE']
        + ";UID="
        + st.secrets['USERNAME']
        + ";PWD="
        + st.secrets['PASSWORD']
 
    )
 
connection = init_connection()
 
@st.cache_data(show_spinner='running_query...')
def running_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        #st.write(cursor.description)
        df = pd.DataFrame.from_records(rows, columns=[column[0] for column in cursor.description])
 
    return df
 
 
def get_all_column():
    sql_query = " SELECT * FROM LP2_Telco_churn_first_3000"
    return running_query(sql_query)
 
df = get_all_column()
 
 
numerical_columns = df.select_dtypes(include=['number']).columns
categorical_columns = df.select_dtypes(exclude=['number']).columns
 
option = st.selectbox('Select..', options=['All columns', 'Numerical columns', 'Categorical columns'])
 
if option == 'All columns':
    st.write(df)
elif option == 'Numerical columns':
    st.write(df[numerical_columns])
elif option == 'Categorical columns':
    st.write(df[categorical_columns])