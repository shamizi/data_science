import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import f1_score
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree

def save_prediction(prediction):
    with open("Voting.txt", 'w') as f:
        for pred in prediction:
            #print(pred)
            f.write('Jedi\n' if pred == 'Jedi' else 'Sith\n')


def voting_classifier(train_file, test_file):
    train = pd.read_csv(train_file)
    test = pd.read_csv(test_file)

    # Séparer les features et les labels
    X_train = train.iloc[:, :-1].values  # Toutes les colonnes sauf la dernière pour les features
    y_train = train.iloc[:, -1].values   # La dernière colonne pour les labels
    X_test = test.iloc[:, :-1].values    # Toutes les colonnes sauf la dernière pour les features
    y_test = test.iloc[:, -1].values     # La dernière colonne pour les labels

    # Normalisation des features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    knn = KNeighborsClassifier(n_neighbors=15)
    dt = DecisionTreeClassifier(random_state=42)
    neural = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=200, alpha=0.0001, solver='adam', random_state=42, verbose=True)

    voting_clf = VotingClassifier(estimators=[
        ('knn', knn),
        ('dt', dt),
        ('neural', neural)
        ], voting='hard')
    
    voting_clf.fit(X_train, y_train)
    y_pred = voting_clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')

    print(f"Voting Accuracy: {accuracy:.2f}")
    print(f"Voting F1 Score: {f1:.2f}")

def neural_network(train_file, test_file):
    train = pd.read_csv(train_file)
    test = pd.read_csv(test_file)

    X_train = train.iloc[:, :-1].values  # Toutes les colonnes sauf la dernière pour les features
    y_train = train.iloc[:, -1].values   # La dernière colonne pour les labels
    X_test = test.iloc[:, :-1].values    # Toutes les colonnes sauf la dernière pour les features
    y_test = test.iloc[:, -1].values     # La dernière colonne pour les labels

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    mlp = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=200, alpha=0.0001, solver='adam', random_state=42, verbose=True)
    mlp.fit(X_train, y_train)
    y_pred = mlp.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    save_prediction(y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print(f"F1 Score: {f1:.2f}")


neural_network("C:/Users/said/Desktop/data_science/day05/Training_knight.csv", "C:/Users/said/Desktop/data_science/day05/Validation_knight.csv")
voting_classifier("C:/Users/said/Desktop/data_science/day05/Training_knight.csv", "C:/Users/said/Desktop/data_science/day05/Validation_knight.csv")