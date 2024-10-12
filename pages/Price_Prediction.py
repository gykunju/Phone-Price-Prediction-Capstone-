import streamlit as st 
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
import joblib
import final_model

scaler = joblib.load('scaler.pkl')
poly = joblib.load('poly.pkl')
ridge = joblib.load('ridge_model.pkl')

data = pd.read_csv('./final_data.csv')

st.title('Price Estimator Model')

st.subheader('Enter the prompted values to get a price estimation')

col1,col2,col3,col4 = st.columns(4)

display_size = col1.number_input('Display Size')
refresh_rate = col2.number_input('Refresh Rate')
px_width = col3.number_input('Pixel Width')
px_height = col4.number_input('Pixel Height')

col1,col2,col3,col4 = st.columns(4)

ram = col1.number_input('RAM')
storage = col2.number_input('Storage')
battery = col3.number_input('Battery')
brand = col4.text_input('Brand')

col1,col2,col3,col4 = st.columns(4)
fc = col1.number_input('Front Cam')
rc = col2.number_input('Rear Cam')
processor = col3.text_input('Processor')
year = col4.date_input('Year')

def Predict():
    brand_label = list(data['Brand'].sort_values().unique()).index(brand.strip())
    processor_label = list(data['Processor'].sort_values().unique()).index(processor)
    days = (pd.Timestamp('2024-10-12') - pd.Timestamp(str(year))).days
    row = pd.DataFrame([[display_size, refresh_rate, rc, fc, ram, storage, battery, px_width, px_height, days, processor_label, brand_label]])

    row_scaled = scaler.transform(row) 
    
    row_poly = poly.transform(row_scaled) 

    # predicting
    prediction = ridge.predict(row_poly)
    
    # Store the prediction in session state
    st.session_state['Prediction'] = prediction

st.button('Estimate Price', on_click=Predict)

if 'Prediction' not in st.session_state:
    st.session_state['Prediction'] = 'N/A'

st.success(f'Price Estimate: {st.session_state["Prediction"]}') 