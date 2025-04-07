import numpy as np
import pandas as pd
import zipfile
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

zip_file_path = r"C:\Users\Artur\Downloads\car+evaluation.zip"

with zipfile.ZipFile(zip_file_path, 'r') as z:
    with z.open('car.data') as f:
        df = pd.read_csv(f, header=None)

df.columns = ['Buying', 'Maint', 'Doors', 'Persons', 'Lug_boot', 'Safety', 'Class']
df_encoded = pd.get_dummies(df, columns=['Buying', 'Maint', 'Doors', 'Persons', 'Lug_boot', 'Safety'])

X = df_encoded.drop(columns="Class")
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train,y_train)
y_pred = tree.predict(X_test)
print(y_pred[:5])
print(y_test[:5].values)
acc = accuracy_score(y_test, y_pred)
print(f"{acc*100:.2f}%")