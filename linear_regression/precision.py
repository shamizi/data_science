import pandas as pd
import numpy as np
import os
import sys
sys.path.append("C:/Users/said/Desktop/data_science/linear_regression")
from estimate_price import estimateprice

def load_theta_values(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) == 2:
                real_theta0 = float(lines[0].strip())
                real_theta1 = float(lines[1].strip())
                return real_theta0, real_theta1
    return None, None

def calculate_metrics(data_path, theta0, theta1):
    data = pd.read_csv(data_path)
    km = data['km'].values
    price = data['price'].values

    # Predict the prices using the model parameters
    predicted_prices = estimateprice(km, theta0, theta1)

    # Calculate Mean Squared Error (MSE)
    mse = np.mean((price - predicted_prices) ** 2)

    # Calculate Mean Absolute Error (MAE)
    mae = np.mean(np.abs(price - predicted_prices))

    # Calculate R-squared (R²)
    ss_total = np.sum((price - np.mean(price)) ** 2)
    ss_residual = np.sum((price - predicted_prices) ** 2)
    r_squared = 1 - (ss_residual / ss_total)

    # Calculate Mean Absolute Percentage Error (MAPE)
    mape = np.mean(np.abs((price - predicted_prices) / price)) * 100

    return mse, mae, r_squared, mape

def main():
    data_path = "C:/Users/said/Desktop/data_science/linear_regression/data.csv"
    theta_file_path = 'theta_values.txt'

    # Load theta values
    theta0, theta1 = load_theta_values(theta_file_path)
    if theta0 is None or theta1 is None:
        print("Model parameters not found. Please train the model first.")
        return

    # Calculate metrics
    mse, mae, r_squared, mape = calculate_metrics(data_path, theta0, theta1)

    # Print the metrics
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"R-squared (R²): {r_squared}")
    print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")

if __name__ == "__main__":
    main()
