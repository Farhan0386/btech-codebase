import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Load your data (paste your data into a file named 'marks.txt')
# Assuming data is comma-separated
data = pd.read_csv('marks.txt', header=None, names=['Exam1', 'Exam2', 'Label'])

# 2. Separate features (X) from the target label (y)
X = data[['Exam1', 'Exam2']]
y = data['Label']

# 3. Split data into Training set (80%) and Testing set (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize the Logistic Regression Model
model = LogisticRegression()

# 5. Train the model using the training data
model.fit(X_train, y_train)

# 6. Make predictions on the test data
predictions = model.predict(X_test)

# 7. Check how accurate your model is
accuracy = accuracy_score(y_test, predictions)

print(f"Model Training Complete!")
print(f"Accuracy of your first ML model: {accuracy * 100:.2f}%")

# 8. Test it with your own custom marks!
# Example: What happens if a student gets 60 in Exam 1 and 70 in Exam 2?
custom_student = np.array([[60, 70]])
prediction = model.predict(custom_student)
print(f"Prediction for marks [60, 70]: {'Pass (1)' if prediction[0] == 1 else 'Fail (0)'}")