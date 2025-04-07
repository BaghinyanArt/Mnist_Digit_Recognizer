import pandas as pd 
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("C:/Users/Artur/Downloads/car.data")
df.columns = ['Buying', 'Maint', 'Doors', 'Persons', 'Lug_boot', 'Safety', 'Class']
df_encoded = pd.get_dummies(df, columns=['Buying', 'Maint', 'Doors', 'Persons', 'Lug_boot', 'Safety'])
X = df_encoded.drop(columns="Class")
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)

class MyBootstrapAggregating:
    
    def __init__(self, X_data, y_data, n_tress=5):
        self.X_data = X_data
        self.y_data = y_data
        self.n_tress = n_tress 
        self.models = []
        self.predictions = []

    def fit(self):
        for i in range(self.n_tress):
            model = DecisionTreeClassifier(random_state=i) 
            model.fit(self.X_data, self.y_data) 
            self.models.append(model)  
            preds = model.predict(self.X_data) 
            self.predictions.append(preds)

    def predict(self):
        predictions= np.array(self.predictions)
        final_predictions = []
        for i in range(predictions.shape[1]):  
            column_predictions = predictions[:, i]  
            most_common = Counter(column_predictions).most_common(1)[0][0]  
            final_predictions.append(most_common)

        return final_predictions
    

b1 = MyBootstrapAggregating(X_train,y_train)
b2 = MyBootstrapAggregating(X_test,y_test)

b1.fit()
train_predictions = b1.predict()

b2.fit()
test_predictions = b2.predict()

print("Training set predictions (first 5):", train_predictions[:10])
print("Test set predictions (first 5):", test_predictions[:10])