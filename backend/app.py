""" 
Flask API backend providing endpoints for predictive maintenance.
"""
from flask import Flask, jsonify, request
from config import Config
from database import get_db_connection
import pickle
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
app.config.from_object(Config)

# Load saved models (ensure models are trained beforehand)
lstm_model = load_model("model/model_lstm.h5")
with open("model/model_rf.pkl", "rb") as f:
    rf_model = pickle.load(f)

@app.route("/api/status", methods=["GET"])
def get_truck_status():
    """Endpoint to return truck status from the database."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM truck_status;")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)

@app.route("/api/predict", methods=["POST"])
def predict():
    """Endpoint to perform prediction on sensor data."""
    data = request.json  # Expected to be a list of sensor values for a truck over time
    # Assume data is preprocessed into the correct shape: (timesteps, 1)
    X = np.array(data).reshape((1, len(data), 1))
    lstm_pred = lstm_model.predict(X)
    rf_pred = rf_model.predict(lstm_pred)
    return jsonify({"prediction": int(rf_pred[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
