import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from statsmodels.stats.outliers_influence import variance_inflation_factor


def variance(path_file):
    train = pd.read_csv(path_file)

    features = train.iloc[:, :-1]
    scaler = StandardScaler()
    scaled_featured = scaler.fit_transform(features)

    pca = PCA()
    pca.fit(scaled_featured)
    variance = pca.explained_variance_ratio_ * 100

    cumulative_variance = np.cumsum(variance)
    plt.figure(figsize=(10, 5))
    plt.plot(cumulative_variance, marker='o')
    plt.axhline(y=90, color='r', linestyle='--')
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance (%)')
    plt.title('Cumulative Explained Variance')
    plt.grid(True)
    plt.show()
    print(variance)
    print(cumulative_variance)



variance("C:/Users/said/Desktop/data_science/day05/Train_knight.csv")