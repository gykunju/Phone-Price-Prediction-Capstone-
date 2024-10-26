# 📱 Kenyan Phone Price Estimator
This project aims to provide accurate price predictions for mobile phones in Kenya based on key specifications, brand, and release date. The Phone Price Estimator helps both buyers and sellers by offering a price benchmark tailored to the Kenyan market, addressing a crucial challenge in valuing mobile devices.

## 📝 Overview
Mobile phones have become indispensable in today's world, serving vital roles in communication, information access, and recreation. However, determining a fair price for a phone in the Kenyan market can be challenging due to the variety of brands, models, and specifications available. This project uses machine learning techniques to estimate phone prices based on local data and specifications.

## 💾 Data Source
The dataset was collected from major Kenyan phone marketplaces like Phone Place Kenya with technical specs referenced from international sites such as Phone Arena and GSMArena. Factors such as brand reputation, display size, camera quality, battery life, and release date were considered for price estimation.

## 🛠️ Features and Engineering
The following features were extracted and preprocessed:

Display Size: The screen size in inches.
Refresh Rate: Refresh rate of the display in Hz.
Pixel Dimensions: Screen resolution split into pixel width and height.
RAM and Storage: Memory and internal storage capacity in GB.
Battery: Battery capacity in mAh.
Brand: Manufacturer of the phone.
Camera Quality: Front and rear camera resolutions in MP.
Processor: Processor model.
Release Date: Converted into "days since release" to account for the age of the device.
## 🔍 Exploratory Data Analysis (EDA)
The EDA component provides insights into the pricing distribution, price trends over time, and comparisons across brands. Key findings include:

Brand Analysis: Some brands, like Motorola, maintain higher average prices, while Samsung and Huawei offer a wider range of prices.
Feature Correlations: Display size, RAM, and storage show a positive correlation with price.
Market Trends: A general price increase trend over the years, particularly evident in Samsung's lineup.
## 🔮 Price Prediction Model
The price prediction model uses a combination of polynomial transformations and ridge regression to handle non-linear relationships among features. Key steps in model development:

Scaling: StandardScaler was applied for uniform scaling.
Polynomial Transformation: Features were transformed to a degree of 2 to capture complex relationships.
Regularization: Ridge regression was chosen to mitigate overfitting, with an optimal alpha value of 10.
Performance: The final model achieved an R² score of approximately 0.63 on test data, providing reasonable accuracy in price prediction.
## 🔧 How to Use

Launch the Streamlit app for Exploratory Data Analysis (EDA) and Price Estimation:
bash

Enter Specifications:

Input phone specs such as display size, RAM, storage, and release year to get an estimated price.
## 📊 Screenshots
Price Distribution by Brand: Shows average prices per brand.
![Screenshot 2024-10-26 065004](https://github.com/user-attachments/assets/b39de78e-8bd1-47f7-91f4-a839de18a672)

Price Prediction Interface: Enter phone specifications to get a price estimate in Kenyan Shillings.
![Predictor](https://github.com/user-attachments/assets/488d123c-48ce-4f50-a7b0-31ae7e4aa4d7)
