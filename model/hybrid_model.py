""" 
Defines a hybrid model combining LSTM for time-series forecasting and Random Forest for anomaly detection.
"""
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.ensemble import RandomForestClassifier
import pickle

def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=input_shape))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

def train_hybrid_model(X_train, y_train, lstm_epochs=10):
    # Reshape X_train for LSTM: (samples, timesteps, features)
    X_train_lstm = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    lstm_model = build_lstm_model((X_train_lstm.shape[1], 1))
    lstm_model.fit(X_train_lstm, y_train, epochs=lstm_epochs, verbose=1)
    
    # Use LSTM predictions as features for Random Forest
    lstm_predictions = lstm_model.predict(X_train_lstm)
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(lstm_predictions, y_train)
    
    # Save models
    lstm_model.save("model_lstm.h5")
    with open("model_rf.pkl", "wb") as f:
        pickle.dump(rf_model, f)
    
    return lstm_model, rf_model
