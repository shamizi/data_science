import pandas as pd
import matplotlib.pyplot as plt

def create_histo(file_path):
    df = pd.read_csv(file_path)
    num_columns = len(df.columns)
    
    # Calculer le nombre de lignes et de colonnes pour les sous-graphiques
    rows = (num_columns + 2) // 5
    cols = 5

    fig, axes = plt.subplots(rows, cols, figsize=(25, 5 * rows))
    axes = axes.flatten()

    for i, column in enumerate(df.columns):
        axes[i].hist(df[column], bins=40, color='green') 
        axes[i].set_title(column)
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Frequency')

    
    # Supprimer les sous-graphiques vides
    for i in range(len(df.columns), len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()

def jedi_vs_sith(file_path):
    df = pd.read_csv(file_path)
    num_columns = len(df.columns) - 1
    jedi = df[df['knight'] == 'Jedi']
    sith = df[df['knight'] == 'Sith']
    
    # Calculer le nombre de lignes et de colonnes pour les sous-graphiques
    rows = (num_columns + 2) // 5
    cols = 5

    fig, axes = plt.subplots(rows, cols, figsize=(25, 5 * rows))
    axes = axes.flatten()

    for i, column in enumerate(df.columns):
        if column != 'knight':
            axes[i].hist(jedi[column], bins=40, color='blue', alpha=0.3) 
            axes[i].hist(sith[column], bins=40, color='red', alpha=0.3) 
            axes[i].set_title(column)
            axes[i].set_xlabel(column)
            axes[i].set_ylabel('Frequency')

    
    # Supprimer les sous-graphiques vides
    for i in range(len(df.columns), len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()


#create_histo("C:/Users/said/Desktop/data_science/day04/Test_knight.csv")
jedi_vs_sith("C:/Users/said/Desktop/data_science/day04/Train_knight.csv")