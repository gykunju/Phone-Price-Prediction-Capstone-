import streamlit as st
import pandas as pd

st.title('Phone Price Estimator')

st.sidebar.success('Select a Page')

st.write('The valuation of a mobile device has been a major problem for both sellers and buyers of the devices')
st.write('Numerous Factors like the specs of the device, the brand that created it and the year of production play a very major role in the price estimation of a phone in the modern age')

st.write('This project is meant to make the price estimation align with the current view based on a few characteristics')


st.header('Data')

st.write('The data was aquired from one of the major and might I say ''standard'' of Kenyan phone pricing (Phone Place Kenyan)')

data = pd.read_csv('./phones_data.csv')
data.drop(columns=['Unnamed: 0'], inplace=True)

st.write('This is the data structure:')

st.expander('Phone Data').dataframe(data)

column_descriptions = {
    "Display Size": "The diagonal size of the phone's display in inches.",
    "Refresh Rate": "The rate at which the display refreshes in Hz (higher is smoother).",
    "Pixel Width": "The width of the screen resolution in pixels.",
    "Pixel Height": "The height of the screen resolution in pixels.",
    "RAM": "The amount of memory available in gigabytes (GB).",
    "Storage": "The internal storage space of the phone in gigabytes (GB).",
    "Battery": "The battery capacity in milliampere-hour (mAh).",
    "Brand": "The manufacturer of the phone (e.g., Samsung, Apple).",
    "Front Cam": "The resolution of the front-facing camera in megapixels (MP).",
    "Rear Cam": "The resolution of the rear-facing camera in megapixels (MP).",
    "Processor": "The name or model of the phone's processor (SoC).",
    "Release Date": "The year the phone was released or manufactured."
}

st.title("Phone Specification Descriptions")

# Display column names and descriptions
for column, description in column_descriptions.items():
    st.write(f"**{column}:** {description}")