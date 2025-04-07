import numpy as np
import pandas as pd
import zipfile

zip_file_path = r"C:\Users\Artur\Downloads\car+evaluation.zip"

with zipfile.ZipFile(zip_file_path, 'r') as z:
    with z.open('car.data') as f:
        df = pd.read_csv(f, header=None)

df.columns = ['Buying', 'Maint', 'Doors', 'Persons', 'Lug_boot', 'Safety', 'Class']

class DecisionTree:
    def __init__(self, max_depth=5):
        self.max_depth = max_depth
        self.tree = None

    def gini_impurity(self, y):
        class_counts = y.value_counts()
        total = len(y)
        gini = 1.0  
        for count in class_counts:
            prob = count / total  
            gini -= prob ** 2 
        return gini

    def split_dataset(self, X, y, feature, value):
        left_mask = X[feature] == value 
        right_mask = ~left_mask
        X_left, X_right = X[left_mask], X[right_mask]
        y_left, y_right = y[left_mask], y[right_mask]
        return X_left, X_right, y_left, y_right

    def best_feature_to_split(self, X, y):
        best_gini = float('inf') 
        best_feature = None
        best_value = None

        for feature in X.columns:
            possible_values = X[feature].unique()
            for value in possible_values:
                X_left, X_right, y_left, y_right = self.split_dataset(X, y, feature, value)
                gini_left = self.gini_impurity(y_left)
                gini_right = self.gini_impurity(y_right)
                weighted_gini = (len(y_left) / len(y)) * gini_left + (len(y_right) / len(y)) * gini_right
                if weighted_gini < best_gini:
                    best_gini = weighted_gini
                    best_feature = feature
                    best_value = value

        return best_feature, best_value, best_gini
    
    def build_tree(self, X, y, depth=0):
        if len(y.unique()) == 1: 
            return y.iloc[0]
        
        if depth == self.max_depth: 
            return y.mode()[0]
        best_feature, best_value, best_gini = self.best_feature_to_split(X, y)
        X_left, X_right, y_left, y_right = self.split_dataset(X, y, best_feature, best_value)
        left_tree = self.build_tree(X_left, y_left, depth + 1)
        right_tree = self.build_tree(X_right, y_right, depth + 1)
        return {
            'feature': best_feature,
            'value': best_value,
            'left': left_tree,
            'right': right_tree
        }
tree = DecisionTree(max_depth=5)
X = df.drop(columns='Class') 
y = df['Class'] 
tree_structure = tree.build_tree(X, y)
print(tree_structure)
