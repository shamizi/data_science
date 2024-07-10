import pandas as pd
from sklearn.model_selection import train_test_split

def split(file_path):
    df = pd.read_csv(file_path)
    Training_knight, Validation_knight = train_test_split(df, test_size=0.2)
    Training_knight.to_csv("Training_knight.csv")
    Validation_knight.to_csv("Validation_knight.csv")

    print(Training_knight)
    print(Validation_knight)

split("C:/Users/said/Desktop/data_science/day04/Train_knight.csv")