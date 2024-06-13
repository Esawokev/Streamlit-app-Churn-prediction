#Get the necessary libraries
import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from imblearn.pipeline import Pipeline as ImbPipeline

# Page configaration
st.set_page_config(
    page_title='Prediction Page',
    page_icon=':chat:',
    layout='wide'
)

# Page title
st.title('Predict Churn Probability')


# Loading the pipelines(models)
@st.cache_resource()
def load_forest_pipeline():
    return joblib.load('./Models/forest_pipeline.joblib')

@st.cache_resource()
def load_logistic_pipeline():
    return joblib.load('./Models/logistic_pipeline.joblib')

@st.cache_resource()
def load_label_encoder():
    return joblib.load('./Models/label_encoder.joblib')

# Provide the select option
def select_model(selected_model):
    if selected_model == 'Random Forest':
        pipeline = load_forest_pipeline()
    else:
        pipeline = load_logistic_pipeline()
        
    encoder = load_label_encoder()
    return pipeline, encoder

#creat the predict function
def make_prediction(pipeline, encoder):
    # Collect user input from session state
    user_input = {
        'gender': st.session_state.get('gender'),
        'marital_status': st.session_state.get('marital_status'),
        'dependents': st.session_state.get('dependents'),
        'internetservice': st.session_state.get('internetservice'),
        'contract': st.session_state.get('contract'),
        'tenure': st.session_state.get('tenure'),
        'paymentmethod': st.session_state.get('payment_method'),
        'monthlycharges': st.session_state.get('monthly_charges'),
        'totalcharges': st.session_state.get('total_charges'),
        'seniorcitizen': st.session_state.get('seniorcitizen'),
        'paperlessbilling': st.session_state.get('paperlessbilling'),
        'multiplelines': st.session_state.get('multiplelines'),
        'onlinesecurity': st.session_state.get('onlinesecurity'),
        'phoneservice': st.session_state.get('phoneservice'),
        'deviceprotection': st.session_state.get('deviceprotection'),
        'techsupport': st.session_state.get('techsupport'),
        'streamingtv': st.session_state.get('streamingtv'),
        'streamingmovies': st.session_state.get('streamingmovies'),
        'onlinebackup': st.session_state.get('onlinebackup')
    }
    
    # create dataframe from the imput by users
    df = pd.DataFrame([user_input])

    # Extract expected columns from the preprocessor step in the pipeline
    if 'preprocessor' in pipeline.named_steps:
        preprocessor = pipeline.named_steps['preprocessor']
        if hasattr(preprocessor, 'transformers_'):
            expected_columns = []
            for transformer in preprocessor.transformers_:
                if transformer[1] != 'drop':
                    expected_columns.extend(transformer[2])
    else:
        expected_columns = df.columns.tolist()

    # Add any missing columns with default values
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0

    try:
        pred = pipeline.predict(df)
        pred_proba = pipeline.predict_proba(df)
        decoded_pred = encoder.inverse_transform(pred)
        st.session_state['prediction'] = decoded_pred[0]  # Save the first prediction only
        st.session_state['probability'] = pred_proba[0][1]*100 
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.session_state['prediction'] = None
        st.session_state['probability'] = None

if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None

if 'probability' not in st.session_state:
    st.session_state['probability'] = None

#create a form
def display_form():
    col1, col2= st.columns(2)
    with col1:
        selected_model = st.selectbox('Select a model', options=['Random Forest', 'Logistic Regression'], key='selected_model')
    global pipeline, encoder
    pipeline, encoder = select_model(selected_model)
    encoder.fit(['No', 'Yes'])

    with st.form('input_features'):
        st.write('### Family Information')
        with st.expander("Customer Info"):
            col1, col2 = st.columns(2)
            with col1:
                st.selectbox('Senior Citizen', options=[0, 1], key='seniorcitizen')
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
                

        st.form_submit_button('Submit', on_click=make_prediction, kwargs=dict(pipeline=pipeline, encoder=encoder))

if __name__ == "__main__":
    display_form()
    final_prediction = st.session_state.get('prediction')
    final_probability = st.session_state.get('probability')

    if final_prediction is None:
        st.write('### No prediction available')
    else:
        st.write(f'## Prediction: {final_prediction}')
        st.write(f'## Probability of this customer churnning is: {final_probability:.2f}%')