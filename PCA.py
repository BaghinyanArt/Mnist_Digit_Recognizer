import numpy as np
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
X = df.values

class PCA:
    """
    Principal Component Analysis (PCA) class to reduce the dimensionality
    of a dataset by projecting it onto the top 'n' principal components.

    Attributes:
        n (int): Number of principal components to retain.
        eigenvectors (np.ndarray): Eigenvectors of the covariance matrix.
        eigenvalues (np.ndarray): Eigenvalues of the covariance matrix.
        mean (np.ndarray): Mean of the input data.
    """
    def __init__(self, n):
        """
        Initializes the PCA object with the number of principal components to retain.

        Args:
            n (int): Number of principal components to compute.
        """
        self.n = n 
        self.eigenvectors = None
        self.eigenvalues = None
        self.mean = None

    def fit(self, X):
        """
        Fits the PCA model to the dataset by computing the covariance matrix,
        eigenvalues, and eigenvectors.

        Args:
            X (np.ndarray): The input data matrix of shape (n_samples, n_features).

        Steps:
            1. Center and standardize the data (mean = 0, variance = 1).
            2. Compute the covariance matrix of the standardized data.
            3. Perform eigenvalue decomposition on the covariance matrix.
            4. Sort eigenvalues and corresponding eigenvectors in descending order.
        """
        self.mean = np.mean(X, axis=0)
        std = np.std(X, axis=0)
        X_centr = (X - self.mean) / std
        cov_matrix = np.cov(X_centr, rowvar=False)
        self.eigenvalues, self.eigenvectors = np.linalg.eigh(cov_matrix)
        sorted_indices = np.argsort(self.eigenvalues)[::-1]
        self.eigenvalues = self.eigenvalues[sorted_indices]
        self.eigenvectors = self.eigenvectors[:, sorted_indices]

    def transform(self, X):
        """
        Projects the input data onto the top 'n' principal components.

        Args:
            X (np.ndarray): The input data matrix of shape (n_samples, n_features).

        Returns:
            np.ndarray: Transformed data of shape (n_samples, n_components),
                        where 'n_components' is the number of principal components.
        """
        std = np.std(X, axis=0)
        X_centr = (X - self.mean) / std 
        return np.dot(X_centr, self.eigenvectors[:, :self.n])

p = PCA(2)
p.fit(X)
X_new= p.transform(X)
print(X_new)