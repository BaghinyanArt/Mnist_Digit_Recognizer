import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
'Y' : [1, 2, 3, 4, 5], # Region
'X1'   : [50, 100, 150, 200, 250], # Area in square kilometers
'X2' : [17, 20, 16, 22, 25] # Average temperature in Celsius
}

df = pd.DataFrame(data)

X = df[['X1', 'X2']] 
Y  = df['Y']           
model = LinearRegression()
model.fit(X, Y)
Y_pred = model.predict(X)

sse = np.sum((Y - Y_pred) ** 2)
sst = np.sum((Y - np.mean(Y)) ** 2)
r_2 = 1 - (sse / sst)
n = len(Y)  
p = X.shape[1] 
adj_r_2 = 1 - ((1 - r_2) * (n - 1)) / (n - p - 1)
mse = sse / n
rmse = np.sqrt(mse)