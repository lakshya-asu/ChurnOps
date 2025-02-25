from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load("model/churn_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    # Expect a JSON payload with a key "features" containing feature data.
    data = request.get_json(force=True)
    input_data = pd.DataFrame([data["features"]])
    
    # Predict churn (for logistic regression, output is 0 or 1)
    prediction = model.predict(input_data)[0]
    
    # Optionally, provide prediction probabilities
    # prob = model.predict_proba(input_data)[0].tolist()
    
    return jsonify({"prediction": int(prediction)})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    # Run the API on host 0.0.0.0 and port 5000
    app.run(host="0.0.0.0", port=5000)
