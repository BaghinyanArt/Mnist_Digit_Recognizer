# Առաջադրանք 1
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn import datasets
# from sklearn.decomposition import PCA
# from sklearn.preprocessing import StandardScaler

# wine = datasets.load_wine()
# df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
# df["target"] = wine.target 
# if df.isnull().values.any():
#     print("There are NaN values in the DataFrame.")
# else:
#     print("No NaN values found.")
# scaler = StandardScaler()
# df_sta = scaler.fit_transform(df)    
# pca = PCA(n_components=3)
# wine_pca = pca.fit_transform(df_sta)
# new_df = pd.DataFrame(data=wine_pca, columns=["col1","col2","col3"])
# new_df["target"] = wine.target
# explained_variance = pca.explained_variance_ratio_
# total_explained_variance = explained_variance.sum() * 100
# print(f"Explained variance for col1: {explained_variance[0] * 100:.2f}%")
# print(f"Explained variance for col2: {explained_variance[1] * 100:.2f}%")
# print(f"Explained variance for col3: {explained_variance[2] * 100:.2f}%")
# plt.figure(figsize=(8, 5))
# plt.plot(range(1, len(explained_variance) + 1), explained_variance * 100, marker='o', linestyle='--')
# plt.title('Scree Plot')
# plt.xlabel('Principal Components')
# plt.ylabel('Explained Variance (%)')
# plt.xticks(range(1, len(explained_variance) + 1))  
# plt.grid()
# plt.show()
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
# scatter = ax.scatter(new_df["col1"], new_df["col2"], new_df["col3"], c=new_df["target"], cmap='viridis', s=50)
# ax.set_title('3D PCA of Wine Dataset', fontsize=16)
# ax.set_xlabel('Principal Component 1 (col1)', fontsize=12)
# ax.set_ylabel('Principal Component 2 (col2)', fontsize=12)
# ax.set_zlabel('Principal Component 3 (col3)', fontsize=12)
# cbar = plt.colorbar(scatter)
# cbar.set_label('Target Class', fontsize=12)
# plt.show()
# Առաջադրանք 2
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

wine = datasets.load_wine()
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
df['target'] = df['alcohol']
X = df.drop(columns=['target'])
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse_without_pca = mean_squared_error(y_test, y_pred)
r2_without_pca = r2_score(y_test, y_pred)

print(f"Linear Regression without PCA:")
print(f"Mean Squared Error: {mse_without_pca:.2f}")
print(f"R^2 Score: {r2_without_pca:.2f}\n")

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

pca = PCA(n_components=3)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

model_pca = LinearRegression()
model_pca.fit(X_train_pca, y_train)

y_pred_pca = model_pca.predict(X_test_pca)
mse_with_pca = mean_squared_error(y_test, y_pred_pca)
r2_with_pca = r2_score(y_test, y_pred_pca)

print(f"Linear Regression with PCA:")
print(f"Mean Squared Error: {mse_with_pca:.2f}")
print(f"R^2 Score: {r2_with_pca:.2f}")
