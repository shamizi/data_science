import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score

def save_prediction(prediction):
    with open("Tree.txt", 'w') as f:
        for pred in prediction:
            #print(pred)
            f.write('Jedi\n' if pred == 'Jedi' else 'Sith\n')

def tree(train_file, test_file):
    train = pd.read_csv(train_file)
    test = pd.read_csv(test_file)

    X_train = train.iloc[:, :-1].values  # Toutes les colonnes sauf la dernière pour les features
    y_train = train.iloc[:, -1].values   # La dernière colonne pour les labels
    X_test = test.iloc[:, :-1].values    # Toutes les colonnes sauf la dernière pour les features
    y_test = test.iloc[:, -1].values     # La dernière colonne pour les labels

    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(X_train, y_train)
    y_pred_dt = decision_tree.predict(X_test)

    accuracy_dt = accuracy_score(y_test, y_pred_dt)
    f1_dt = f1_score(y_test, y_pred_dt, average='weighted', labels=['Jedi', 'Sith'])
    save_prediction(y_pred_dt)
    print("precision = ", accuracy_dt)
    print("f1 score = ",f1_dt)
    plt.figure(figsize=(20,10))
    plot_tree(decision_tree, feature_names=train.columns[:-1], class_names=[str(i) for i in set(y_train)],
              filled=True,rounded=True ,fontsize=6,proportion=True)
    plt.show()

tree("C:/Users/said/Desktop/data_science/day05/Training_knight.csv", "C:/Users/said/Desktop/data_science/day05/Validation_knight.csv")