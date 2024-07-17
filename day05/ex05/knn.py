import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt

def knn(train_file, test_file):
    train = pd.read_csv(train_file)
    test = pd.read_csv(test_file)

    X_train = train.iloc[:, :-1].values  # Toutes les colonnes sauf la dernière pour les features
    y_train = train.iloc[:, -1].values   # La dernière colonne pour les labels
    X_test = test.iloc[:, :-1].values    # Toutes les colonnes sauf la dernière pour les features
    y_test = test.iloc[:, -1].values     # La dernière colonne pour les labels

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    k_value = range(1, 30)
    accuracies = []
    for k in k_value:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies.append(accuracy)
        f1_dt = f1_score(y_test, y_pred, average='weighted', labels=['Jedi', 'Sith'])
        print(f"accuracy {k} = {accuracy}")
        print(f"f1_score {k}  = {f1_dt}")
    plt.figure(figsize=(10, 6))
    plt.plot(k_value, accuracies, marker=None, linestyle='-', color='b')
    plt.title('Accuracy')
    plt.xlabel('k value')
    plt.ylabel('Accuracy')
    plt.xticks(range(0, 31, 5))
    plt.grid(False)
    plt.show()


knn("C:/Users/said/Desktop/data_science/day05/Training_knight.csv", "C:/Users/said/Desktop/data_science/day05/Validation_knight.csv")