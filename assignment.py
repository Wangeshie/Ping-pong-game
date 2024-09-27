# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data  # Features
y = iris.target  # Labels (species)

# Split the data into training (70%) and testing (30%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Support Vector Machine (SVM) model
model = SVC(kernel='linear')  # Linear kernel SVM
model.fit(X_train, y_train)

# Test the model on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Predict on a new sample data point
sample_data = [[5.1, 3.5, 1.4, 0.2]]  # Example input (features of a flower)
prediction = model.predict(sample_data)
species = iris.target_names[prediction][0]
print(f"Predicted species for the sample data point: {species}")

# (Optional) Visualize the classification results using a simple plot
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k', s=100)
plt.title("Iris Dataset Visualization (First two features)")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.show()