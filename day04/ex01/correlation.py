import pandas as pd

def correlation(file_path):
    df = pd.read_csv(file_path)
    df['knight'] = df['knight'].apply(lambda x: 0 if x == 'Jedi' else 1)

    
    # Ajouter la colonne knight_num pour le calcul des corrélations

    correlations = df.corr()['knight']
    
    # Trier les corrélations par valeur absolue (de la plus forte à la plus faible)
    correlations = correlations.abs().sort_values(ascending=False)

    print("\nFacteurs de corrélation avec la cible 'knight':")
    print(correlations.round(6))

correlation("C:/Users/said/Desktop/data_science/day04/Train_knight.csv")
