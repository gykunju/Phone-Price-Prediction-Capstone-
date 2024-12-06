# 📱 Kenyan Phone Price Estimator
This project provides accurate price predictions for mobile phones in Kenya based on key specifications, brand, and release date. The **Kenyan Phone Price Estimator** is designed to help buyers and sellers make informed decisions by offering a price benchmark tailored to the Kenyan market.

---

## 📝 Overview
Mobile phones play an essential role in modern life, yet pricing them fairly in the Kenyan market can be challenging. This project leverages **machine learning** to predict phone prices based on local market trends and technical specifications, bridging the gap in valuing mobile devices.

---

## 📂 Features at a Glance
- **Streamlit App** for easy price estimation and exploratory data analysis (EDA).
- **Interactive Visualizations** to explore trends in the Kenyan phone market.
- **Data-driven Price Predictions** based on technical specifications like RAM, storage, and battery life.

### **Screenshots**
#### 1️⃣ Price Distribution by Brand
Explore average prices across major brands:  
![Price Distribution by Brand](https://github.com/user-attachments/assets/b39de78e-8bd1-47f7-91f4-a839de18a672)

#### 2️⃣ Price Prediction Interface
Input phone specifications to get a price estimate in Kenyan Shillings:  
![Price Prediction Interface](https://github.com/user-attachments/assets/488d123c-48ce-4f50-a7b0-31ae7e4aa4d7)

---

## 💾 Data Source
Data was curated from:
- **Kenyan marketplaces**: Platforms like *Phone Place Kenya*.
- **International specs sites**: References from *Phone Arena* and *GSMArena*.

**Features considered for prediction**:
- Brand reputation
- Display size
- Camera quality
- Battery capacity
- Release date

---

## 📊 Exploratory Data Analysis (EDA)
Key findings from our analysis:
- **Brand Trends**: Brands like Motorola have higher average prices, while Samsung offers options across all price ranges.
- **Feature Correlations**: Larger displays, higher RAM, and more storage correlate strongly with higher prices.
- **Market Insights**: Prices have increased over time, particularly in Samsung’s premium models.

### Example Visualizations
- **Price Trends Over Time**:  
  ![Trend Analysis](https://via.placeholder.com/600x400?text=Trend+Visualization)

- **Feature vs. Price Correlation**:  
  ![Correlation Analysis](https://via.placeholder.com/600x400?text=Correlation+Visualization)

---

## 🔮 Price Prediction Model
Our machine learning pipeline includes:
1. **Feature Engineering**:
   - Converting release date to "days since release."
   - Extracting features like resolution (width × height) and polynomial transformations.
2. **Model Training**:
   - Ridge regression with a polynomial degree of 2 to capture non-linear relationships.
   - Optimized regularization to minimize overfitting.
3. **Performance**:
   - Achieved an R² score of **0.63** on test data.

---

## 🚀 How to Use
### 1️⃣ Run the App
Launch the Streamlit app to access both the **EDA** and **Price Estimation** tools:
```bash
streamlit run app.py
