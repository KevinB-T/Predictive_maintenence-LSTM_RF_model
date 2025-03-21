""" 
Utility functions for data preprocessing.
"""
import numpy as np

def preprocess_data(df, target):
    # Normalize the data using min-max normalization.
    X = (df - df.min()) / (df.max() - df.min())
    y = target.values
    
    # For demonstration, use a sliding window of 10 timesteps.
    if len(X) < 10:
        raise ValueError("Not enough data for a sliding window.")
    X_windows = []
    y_windows = []
    for i in range(len(X) - 9):
        window = X.iloc[i:i+10].values
        X_windows.append(window)
        y_windows.append(y[i+9])
    return np.array(X_windows), np.array(y_windows)
