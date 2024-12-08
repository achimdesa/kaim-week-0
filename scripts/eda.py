
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('C:\\Users\\achimdesa\\Downloads\\data\\data\\benin-malanville.csv')


# Step 1: Data Overview
print("Data Shape:", data.shape)
print("\nData Info:")
print(data.info())
print("\nBasic Statistics:")
print(data.describe())

# Step 2: Check for Missing Values
print("\nMissing Values:")
print(data.isnull().sum())

# Step 3: Data Cleaning (Example)
# Dropping rows with missing values (uncomment if needed)
# data.dropna(inplace=True)

# Filling missing values (example: filling with 0)
data.fillna(0, inplace=True)

# Step 4: Data Visualization
# Histograms
data.hist(figsize=(10, 10))
plt.suptitle('Histograms of All Features')
plt.show()

# Box Plots
plt.figure(figsize=(10, 6))
sns.boxplot(data=data)
plt.title('Box Plot of All Features')
plt.show()

# Pair Plots
sns.pairplot(data)
plt.suptitle('Pair Plots of Features', y=1.02)
plt.show()

# Step 5: Correlation Analysis
correlation_matrix = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Save the cleaned data (optional)
data.to_csv('C:\\Users\\achimdesa\\Downloads\\data\\data\\benin_cleaned_data.csv', index=False)