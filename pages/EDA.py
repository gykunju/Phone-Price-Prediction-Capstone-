import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

st.title('Exploratory Data Analysis')

st.write('Highlights Distribution and relations in the dataset')

data = pd.read_csv('./final_data.csv')

data.drop(columns=['Unnamed: 0'], inplace=True)

st.subheader('Data:')

st.expander('Data').dataframe(data)

## Distribution of phones by Price:

st.subheader('Distibution in accordance to Price')

plt.figure(figsize=(5,5))
price_sort = data.sort_values(by='Price').tail(5)

plt.barh(price_sort['Phone_name'], price_sort['Price'], ec='black')

plt.title('Top 10 phones in Price')
plt.grid(axis='x')
sns.despine()

st.pyplot(plt)

## BOTTOM

plt.figure(figsize=(5,5))
price_sort = data.sort_values(by='Price').head(5)

plt.barh(price_sort['Phone_name'], price_sort['Price'], ec='black')

plt.title('Top 10 phones in Price')
plt.grid(axis='x')
sns.despine()

st.pyplot(plt)

st.write('Google pixel 9 pro Fold is the most expensive phone at', data.loc[data['Price'].idxmax()]['Price'], 'while the Nokia 2660 Flip with', data.loc[data['Price'].idxmax()]['Price'],'is the cheapest phone the database')


# CONDUCT A COMPARISON BETWEEN THE MOST EXPENSIVE PHONE AND THE CHEAPEST PHONE

col1, col2 = st.columns(2)


phone_highest_price = data.loc[data['Price'].idxmax()]
phone_lowest_price = data.loc[data['Price'].idxmin()]

col1.metric(phone_highest_price['Phone_name'], phone_highest_price['Price'], phone_highest_price['Processor'])
col2.metric(phone_lowest_price['Phone_name'], phone_lowest_price['Price'], phone_lowest_price['Processor'])
# # Create a comparison table for the two phones
comparison_df = pd.DataFrame({
    'Feature': data.columns,
    'Phone with Highest Price': phone_highest_price,
    'Phone with Lowest Price': phone_lowest_price
}).set_index('Feature')

# # Visualize Numeric Features comparison
numeric_columns = data.select_dtypes(include='number').columns
huge_num = numeric_columns[7:]
small_num = numeric_columns[1:7]

plt.figure(figsize=(8, 8))
comparison_df.loc[huge_num].plot(kind='bar', figsize=(14, 8), width=0.8)
plt.title('Comparison of Numeric Features between Highest and Lowest Priced Phones')
plt.xticks(rotation=45, ha="right")
plt.ylabel('Value')
plt.tight_layout()
st.pyplot(plt)

plt.figure(figsize=(8, 8))
comparison_df.loc[small_num].plot(kind='bar', figsize=(14, 8), width=0.8)
plt.title('Comparison of Numeric Features between Highest and Lowest Priced Phones')
plt.xticks(rotation=45, ha="right")
plt.ylabel('Value')
plt.tight_layout()
st.pyplot(plt)


# # Step 4: Visualize Categorical Features comparison
# categorical_columns = data.select_dtypes(include='object').columns

# for col in categorical_columns:
#     plt.figure(figsize=(8, 4))
#     sns.barplot(x=comparison_df.loc[col].index, y=comparison_df.loc[col].values)
#     plt.title(f'Comparison of {col} between Highest and Lowest Priced Phones')
#     plt.ylabel(col)
#     plt.show()
#     st.pyplot(plt)


# Distribution of Price


plt.figure(figsize=(8, 5))
sns.histplot(data['Price'], kde=True, color='green')
plt.title('Distribution of Price')
st.pyplot(plt)


# Average Price for brands
st.subheader('Brand Price Distribution')

brand_price = data.groupby(by='Brand')['Price'].mean()
brand_price = brand_price.sort_values()

plt.figure(figsize=(8,8))

plt.barh(brand_price.index, brand_price, color='green')

plt.grid(axis='x')
plt.title('Brand Average Price Distribution')
st.pyplot(plt)

st.write('Motorola have the highest average pricing among the brands')

# Price By Brand
st.subheader('Price Distribution by Brand')
plt.figure(figsize=(12, 6))
sns.boxplot(x='Brand', y='Price', data=data)
plt.title('Price Distribution per Brand')
plt.xticks(rotation=45)
st.pyplot(plt)

## Visualizing Samsungs Price Growth
st.subheader('Price Growth over time')
st.write('we will focus on SAMSUNG since it hold majority of the phone instances in the dataset and analyse the trend in price over its years of manufacture')
samsung_data = data[data['Brand'] == 'Samsung'].sort_values('Release Date').set_index('Release Date')

# Create the figure
plt.figure(figsize=(10, 6))

# Plot the data with markers for each point
plt.plot(samsung_data['Price'], marker='o', linestyle='-', color='b')

# Rotate the x-axis labels
plt.xticks(rotation=45, ha='right')

# Add labels and a title
plt.title('Price of Samsung Phones Over Time')
plt.xlabel('Release Date')
plt.ylabel('Price (in $)')

# Show the updated plot in Streamlit
st.pyplot(plt)

st.write('There seems to be an upward Trend By the price')

# Regression plot to see linear relationships

st.subheader('RAM Distribution by Brand')
plt.figure(figsize=(12, 6))
sns.boxplot(x='Brand', y='RAM', data=data)
plt.title('Price Distribution per Brand')
plt.xticks(rotation=45)
st.pyplot(plt)

# RAM and Price
st.subheader('RAM and Price')
plt.figure(figsize=(5, 5))
sns.regplot(x='RAM', y='Price', data=data)
plt.title('Regression plot of RAM vs Price')
st.pyplot(plt)

st.write('An increase in RAM provides a corresponding increase in price (directly proportional)')

# Storage and Price
st.subheader('Storage and Price')
plt.figure(figsize=(5, 5))
sns.regplot(x='Storage', y='Price', data=data)
plt.title('Regression plot of RAM vs Price')
st.pyplot(plt)

st.write('An increase in Storage capacity provides a corresponding increase in price (directly proportional)')



# Front Camera and Rear Camera
st.subheader('Front Camera and Rear Camera')
plt.figure(figsize=(8,8))
sns.regplot(x='Front Camera', y='Rear Camera', data=data)
plt.title('Regression plot of Front Camera vs Rear Camera')
st.pyplot(plt)

st.write('There is a weak relationship between the Front Camera and the Rear Camera')

# RAM and Storage
st.subheader('RAM and Storage')
plt.figure(figsize=(8,8))
sns.regplot(x='RAM', y='Storage', data=data)
plt.title('Regression plot of RAM vs Storage')
st.pyplot(plt)

st.write('From the plot, an increase in the RAM results to a corresponding increase in the Storage')