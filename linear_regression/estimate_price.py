import os

def estimateprice(mileage, theta, theta1):
    return theta + (theta1 * mileage)

def main():
    try:
        test_value = float(input("Please enter the km :"))
    except ValueError:
        print("enter a number and only a number")
        return
    theta0 = 0.0
    theta1 = 0.0
    if os.path.exists('theta_values.txt'):
        with open('theta_values.txt', 'r') as file:
            lines = file.readlines()
            if len(lines) == 2:
                try:
                    theta0 = float(lines[0].strip())
                    theta1 = float(lines[1].strip())
                except ValueError:
                    print("wrong value in .txt")
                    return
                print(f"Using existing theta values from file: theta0 = {theta0}, theta1 = {theta1}")
                estimated_price = estimateprice(test_value, theta0, theta1)
                print(f"Estimated price for {test_value} km is: {estimated_price}")
                return
    else:
            print(estimateprice(test_value,theta0,theta1))
            print("train your data first with linear_regression.py")
    #calculate_theta("C:/Users/said/Desktop/data_science/linear_regression/data.csv", test_value)

if __name__ == "__main__":
    main()