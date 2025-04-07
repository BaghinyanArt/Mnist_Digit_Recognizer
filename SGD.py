import numpy as np

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

class SGD:
    def __init__(self, learning_rate=0.1, n_epochs=50):
        self.learning_rate = learning_rate
        self.n_epochs = n_epochs
        self.theta = None

    def initialize_parameters(self, X):
        """Initialize parameters with a bias term and random weights."""
        m = len(X)
        X_b = np.c_[np.ones((m, 1)), X] 
        self.theta = np.random.randn(X_b.shape[1], 1) 
        return X_b

    def update_parameters(self, xi, yi):
        """Perform a single update of theta based on one sample."""
        prediction = xi.dot(self.theta)
        error = prediction - yi
        gradients = 2 * xi.T.dot(error)
        self.theta -= self.learning_rate * gradients

    def fit(self, X, y):
        """Train the model using stochastic gradient descent."""
        X_b = self.initialize_parameters(X)
        
        for epoch in range(self.n_epochs):
            for i in range(len(X)):
                random_index = np.random.randint(len(X))
                xi = X_b[random_index:random_index + 1]
                yi = y[random_index:random_index + 1]
                self.update_parameters(xi, yi)

    def predict(self, X):
        """Predict using the learned parameters."""
        X_b = np.c_[np.ones((len(X), 1)), X] 
        return X_b.dot(self.theta)

sgd = SGD(learning_rate=0.1, n_epochs=50)
X_b = sgd.initialize_parameters(X)
print("Initialized parameters (theta):", sgd.theta)

random_index = np.random.randint(len(X))
xi = X_b[random_index:random_index + 1]
yi = y[random_index:random_index + 1]
sgd.update_parameters(xi, yi)
print("Parameters (theta) after one update:",sgd.theta)

sgd.fit(X, y)
print("Final parameters (theta) after training:", sgd.theta)

y_pred = sgd.predict(X)
print("Predictions on training data:", y_pred[:10]) 
