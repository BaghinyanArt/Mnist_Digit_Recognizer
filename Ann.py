import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Add a new column with numbers
df['Score'] = [85, 90, 95, 100]

# Display the updated DataFrame


df["Annais uzacy"] = (df["Age"] + df["Score"])/2
print(df.head())