import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append("C:/Users/said/Desktop/data_science/linear_regression")

# Import the estimateprice function
from estimate_price import estimateprice

def calculate_theta(path_file):
    data = pd.read_csv(path_file)
    km = data['km'].values
    price = data['price'].values

    #normalisation
    km_mean = np.mean(km)
    km_std = np.std(km)
    price_mean = np.mean(price)
    price_std = np.std(price)
    
    km_normalized = (km - km_mean) / km_std
    price_normalized = (price - price_mean) / price_std
    
    theta0 = 0
    theta1 = 0

    learningRate = 0.01
    iteration = 1000
    m = len(km)
    
    for _ in range(iteration):
        estimated_prices = estimateprice(km_normalized, theta0, theta1)
        errors = estimated_prices - price_normalized
        sum_errors_theta0 = np.sum(errors)
        sum_errors_theta1 = np.sum(errors * km_normalized)
    
        tmp_theta0 = theta0 - (learningRate * (1/m) * sum_errors_theta0)
        tmp_theta1 = theta1 - (learningRate * (1/m) * sum_errors_theta1)
    
        theta0 = tmp_theta0
        theta1 = tmp_theta1
        if _ % 100 == 0:
            print(f"Iteration {_}: theta0 = {theta0}, theta1 = {theta1}")
        
        #denormaliser :
    real_theta1 = theta1 * (price_std / km_std)
    real_theta = price_mean - real_theta1 * km_mean
    #prediction =estimateprice(test , real_theta, real_theta1)
    print(f"theta0 value : {real_theta}\ntheta1 value : {real_theta1}")
    with open("theta_values.txt", 'w') as file:
        file.write(f"{real_theta}\n")
        file.write(f"{real_theta1}\n")

    plt.scatter(km, price)
    plt.plot(km, estimateprice(km, real_theta, real_theta1), color='red', label='Regression Line')
    plt.xlabel('km')
    plt.ylabel('price')
    plt.show()


def main():
    calculate_theta("C:/Users/said/Desktop/data_science/linear_regression/data.csv")

if __name__ == "__main__":
    main()
