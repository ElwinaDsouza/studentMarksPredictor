# from flask import Flask, request, jsonify
# import joblib
# import numpy as np
# import sqlite3

# app = Flask(__name__)

# # Load ML model
# model = joblib.load("model.pkl")

# # Create SQLite DB and table if not exist
# conn = sqlite3.connect("students.db")
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS students
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#               attendance INTEGER,
#               assignments INTEGER,
#               exam INTEGER,
#               predicted_grade TEXT)''')
# conn.commit()
# conn.close()

# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.json
#     features = np.array([[data["attendance"], data["assignments"], data["exam"]]])
#     pred = model.predict(features)[0]

#     # Save prediction to SQLite
#     conn = sqlite3.connect("students.db")
#     c = conn.cursor()
#     c.execute("INSERT INTO students (attendance, assignments, exam, predicted_grade) VALUES (?, ?, ?, ?)",
#               (data["attendance"], data["assignments"], data["exam"], str(pred)))
#     conn.commit()
#     conn.close()

#     return jsonify({"predicted_grade": str(pred)})

# @app.route("/")
# def home():
#     return "Flask API is running locally!"

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)
# Load trained model
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array([[data["attendance"], data["assignments"], data["exam"]]])
    pred = model.predict(features)[0]

    # Add risk flag
    risk = "High" if pred in ["D", "F"] else "Low"

    # Return prediction + risk directly to frontend
    return jsonify({"predicted_grade": str(pred), "risk": risk})

@app.route("/")
def home():
    return "Flask API is running!"

if __name__ == "__main__":
    app.run(debug=True)
