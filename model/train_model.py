""" 
Script to preprocess data, train the hybrid model, and evaluate performance.
"""
import numpy as np
import pandas as pd
from hybrid_model import train_hybrid_model
from utils import preprocess_data

def main():
    # Generate synthetic training data for demonstration purposes.
    data = pd.DataFrame({
        "temperature": np.random.uniform(-5, 10, 1000),
        "humidity": np.random.uniform(60, 100, 1000),
        "vibration": np.random.uniform(0, 5, 1000),
        "pressure": np.random.uniform(0.8, 1.2, 1000)
    })
    target = (data["temperature"] < 0).astype(int)  # Dummy target: anomaly if temperature < 0

    X_train, y_train = preprocess_data(data, target)
    lstm_model, rf_model = train_hybrid_model(X_train, y_train)

if __name__ == "__main__":
    main()
