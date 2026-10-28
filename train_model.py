import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("student.csv")  # Make sure you have a CSV locally

X = df[['attendance', 'assignments', 'exam']]
y = df['final_grade']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved as model.pkl")
