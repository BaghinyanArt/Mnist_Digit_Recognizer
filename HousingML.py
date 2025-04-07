import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Artur\Downloads\Artur Baghinyan - Housing.csv")
df = pd.DataFrame(data)
df = pd.get_dummies(df, columns=['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus'])
df = df.astype(int)

X = df.drop(columns=['price'])
y = df['price']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"Test R^2 : {r2}")


kf = KFold(n_splits=5, shuffle=True, random_state=42)
price_ranges = []
for train_index, test_index in kf.split(X_scaled):
    X_train, X_test = X_scaled[train_index], X_scaled[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    price_range = (y_pred.min(), y_pred.max())
    price_ranges.append(price_range)

min_prices, max_prices = zip(*price_ranges)

plt.figure(figsize=(10, 6))
plt.plot(range(1, len(min_prices) + 1), min_prices, marker='o', label='Min Price')
plt.plot(range(1, len(max_prices) + 1), max_prices, marker='o', label='Max Price')
plt.title("Price Range for Each Fold in Cross-Validation")
plt.xlabel("Fold Number")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()

r2_scores = cross_val_score(model, X_scaled, y, cv=kf, scoring='r2')
print(f"Cross-validated R^2 scores: {r2_scores}")
mean_r2 = r2_scores.mean()
print(f"Mean Cross-validated R^2: {mean_r2}")



r2_scores = []

for column in X.columns:
    X_column = X[column].values.reshape(-1, 1) 
    
    r2 = cross_val_score(model, X_column, y, cv=5, scoring='r2').mean()
    r2_scores.append((column, r2))

r2_scores.sort(key=lambda x: x[1], reverse=True)

best_column, best_r2 = r2_scores[0]
print(f"The column with the highest R² score is: {best_column} with an R² score of: {best_r2}")

columns, scores = zip(*r2_scores)
plt.figure(figsize=(10, 6))
plt.barh(columns, scores)
plt.xlabel("R² Score")
plt.ylabel("Feature")
plt.title("R² Score for Each Feature (Column) using Cross-Validation")
plt.grid(True)
plt.show()