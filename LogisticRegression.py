import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df = df[df['target'] != 0]
X = df.iloc[:, :-1].values 
y = df['target'].values
y = np.where(y == 2, -1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
y_pred_proba = model.predict_proba(X_test_scaled) 

print(f"Accuracy on test data - {accuracy * 100:.2f}%")
print(f"Recall on test data - {recall * 100:.2f}%")
print(f"Precision on test data - {precision * 100:.2f}%")
print(f"F1-score on test data - {f1 * 100:.2f}%")
print("Confusion Matrix:")
print(cm)
TN, FP = cm[0]  
FN, TP = cm[1] 
print("Confusion Matrix Components:")
print(f"True Negative (TN): {TN} ")
print(f"False Positive (FP): {FP} ")
print(f"False Negative (FN): {FN} ")
print(f"True Positive (TP): {TP} ")

coefficients = model.coef_[0] 
print(coefficients)
for feature, coef in zip(df.columns[:-1], coefficients):
    print(f"{feature}: {coef}")

print("Predicted Probabilities for some samples in the test set:")
print(y_pred_proba[:3])