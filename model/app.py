'''from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Allow React frontend to connect

# Load the model you saved with train_model.py
model = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Validate fields exist
    for field in ['title', 'description', 'requirements']:
        if field not in data:
            return jsonify({'error': f"Missing field: {field}"}), 400

    # Concatenate text fields
    text = (
        str(data['title']).strip() + " " +
        str(data['description']).strip() + " " +
        str(data['requirements']).strip()
    )

    # Predict probabilities
    proba = model.predict_proba([text])[0]
    prediction = int(proba[1] >= 0.5)

    return jsonify({
        'prediction': prediction,
        'probability': proba.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)'''


from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

# Load the trained model
model = joblib.load('model.joblib')

# ✅ Root route for testing in browser
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "✅ Flask Fake Job Predictor API is running!"})

# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Validate required fields
    for field in ['title', 'description', 'requirements']:
        if field not in data:
            return jsonify({'error': f"Missing field: {field}"}), 400

    # Concatenate text fields
    text = (
        str(data['title']).strip() + " " +
        str(data['description']).strip() + " " +
        str(data['requirements']).strip()
    )

    # Predict probabilities
    proba = model.predict_proba([text])[0]
    prediction = int(proba[1] >= 0.5)

    return jsonify({
        "prediction": prediction,
        "probability": proba.tolist()
    })

if __name__ == "__main__":
    # ✅ Bind to 0.0.0.0 so Render/Heroku can access
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
