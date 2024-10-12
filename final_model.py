from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import pandas as pd
import joblib

data = pd.read_csv('./train_data.csv')
data = data.drop(columns=['Unnamed: 0'])

# X and Y
x = data.drop(columns=['Price'])
y = data['Price']

# Scaling
scaler = StandardScaler()

x = scaler.fit_transform(x)


# splitting data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# Poly Transforming

poly = PolynomialFeatures(degree=2)

x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.transform(x_test)

ridge = Ridge(alpha=10)

ridge.fit(x_train_poly, y_train)

joblib.dump(scaler, 'scaler.pkl')
joblib.dump(poly, 'poly.pkl')
joblib.dump(ridge, 'ridge_model.pkl')