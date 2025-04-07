import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
# For binary classification.
df = df[df['target'] != 2]
X = df.iloc[:, :-1].values 
y = df['target'].values
y = np.where(y == 0, -1, 1) 
n_features = X.shape[1]

class Perceptron:
    def __init__(self, n_features, learning_rate=0.01, n_iterations=1000):
        self.w = np.random.randn(n_features) 
        self.b = 0  
        self.learning_rate = learning_rate 
        self.n_iterations = n_iterations

    def predict(self, X):
        linear_output = np.dot(X, self.w) + self.b
        return np.where(linear_output > 0, 1, -1)
    
    def fit(self, X, y):
        for _ in range(self.n_iterations):
            for i in range(X.shape[0]): 
                prediction = self.predict(X[i].reshape(1, -1))  
                if prediction != y[i]:
                    self.w += self.learning_rate * y[i] * X[i]
                    self.b += self.learning_rate * y[i]

per = Perceptron(n_features=n_features, learning_rate=0.01, n_iterations=1000)
per.fit(X, y)
predictions = per.predict(X)
print("First 10 predictions:", predictions[:16])
accuracy = np.mean(predictions == y)
print(f'Accuracy: {accuracy * 100:.2f}%')