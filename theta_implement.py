import numpy as np
import pandas as pd
import json

np.random.seed(10)
babies = range(10)
months = np.arange(13)
data = [(month, np.dot(month, 24.7) + 96 + np.random.normal(loc=0, scale=20))
        for month in months
        for baby in babies]
month_data = [element[0] for element in data]
weight_data = [element[1] for element in data]

class LinearRegression():
    
    def __init__(self):
        self.params = None  
    
    def train(self, data, target):
        X = np.array(data)
        Y = np.array(target)
        X = X.reshape(-1, 1)
        ones_column = np.ones((X.shape[0], 1))
        X_b = np.hstack([ones_column, X])
        XT_X = np.dot(X_b.T, X_b)
        XT_X_inv = np.linalg.inv(XT_X)
        theta = np.dot(XT_X_inv, np.dot(X_b.T, Y))

        self.params = {"b": theta[0], "k": theta[1]}

        with open('params.json', 'w') as file:
            json.dump(self.params, file)
        
        return theta

    def predict(self, month, params_path=None):
        if params_path:
            with open(params_path, 'r') as file:
                self.params = json.load(file)
        
        if self.params is None:
            raise ValueError("At first train the model!")
        
        B = self.params["b"]
        K = self.params["k"]

        weight = (np.array(month) * K) + B
        return weight

m = LinearRegression()
m.train(month_data, weight_data)
print(m.predict(10))     
