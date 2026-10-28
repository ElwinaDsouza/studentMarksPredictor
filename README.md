Student Performance Predictor (Full-Stack ML App)

A full-stack machine learning web application that predicts a student's final grade based on academic and behavioral metrics. The project features a responsive JavaScript frontend, interactive data visualizations, and a Python Flask REST API that serves real-time predictions from a serialized Random Forest Classifier.
** Features**
Real-Time Predictive API: Low-latency REST API built with Flask that takes student data and outputs grade predictions instantly.
Interactive Dashboard: Dynamic data visualization rendering performance metrics and predictive breakdowns using Chart.js.
Asynchronous Architecture: Non-blocking asynchronous POST fetch requests ensuring a fluid, seamless user experience.
 Tech Stack
Frontend: JavaScript (ES6+), Chart.js, HTML5, CSS3
Backend: Python, Flask, REST API
Machine Learning: Scikit-Learn, NumPy, Pandas, Joblib
 System Architecture
1. Frontend UI: User inputs student metrics (Attendance %, Assignment Scores, Exam Grades).
2. Async Request: JavaScript captures inputs and sends an asynchronous JSON POST request to the Flask server.
3. ML Inference: The Flask API unpacks the payload, passes data into the serialized Random Forest model, and generates a prediction.
4. Data Visualization: The API response is parsed by the frontend, dynamically updating the Chart.js dashboard.

 **1. Install Required Dependencies**
Open a terminal (CMD/PowerShell/Linux shell) inside the project folder.
Run:pip install flask flask-cors numpy joblib scikit-learn pandas
**2. Train the Model**
Make sure student.csv is in the same folder.
Run:
python train_model.py
This will create:
model.pkl
(already have it in repository , you can skip this step.)
**3. Run the Backend (Flask API)**
Start the Flask server:
python app.py
You should see:
Flask API is running!
 * Running on http://127.0.0.1:5000/
keep this terminal open.
**Open the Frontend (index.html)**
Simply double-click index.html.
It will open in your browser.
When you click "Predict", it will send a request to:
http://127.0.0.1:5000/predict and display:
Predicted grade
Risk level
Input values

**Repository Structure**

├── studentMarksPredictor
│   ├── train_model.py      # Script to train and evaluate the ML model
│   └── student_model.pkl   # Serialized Random Forest model
│   └──style.css       # Interface styling
│   └── app.js          # Async fetch logic and Chart.js initialization
│   └── index.html          # Application dashboard UI
|   └── app.py                  # Flask application server & API routes
 
