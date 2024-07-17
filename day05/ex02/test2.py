import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler
import numpy as np

def variance(path_file):
    train = pd.read_csv(path_file)
    label_encoder = LabelEncoder()
    scaler = MinMaxScaler()
    df = pd.DataFrame(train)
    
    if 'knight' in df.columns:
        df['knight'] = label_encoder.fit_transform(df["knight"])
    
    # Première partie : Normaliser les données avant de calculer les variances
    numeric_columns = df.select_dtypes(include=[np.number])
    numeric_columns_normalized = pd.DataFrame(scaler.fit_transform(numeric_columns), columns=numeric_columns.columns)
    
    # Calculer la variance de chaque colonne numérique normalisée
    variances = numeric_columns_normalized.var().sort_values(ascending=False).values
    sum_var = variances.sum()
    variances_percent = (variances / sum_var) * 100
    print("Pourcentage des variances normalisées :")
    print(variances_percent)
    
    # Calculer les variances normalisées et leur pourcentage
    variances_normalized = scaler.fit_transform(variances.reshape(-1, 1)).flatten()
    sum_variances_normalized = variances_normalized.sum()
    variances_normalized_percent = (variances_normalized / sum_variances_normalized) * 100
    print("Pourcentage des variances après normalisation :")
    print(variances_normalized_percent)
    
    print("\n\n")
    
    #############################################
    # Seconde partie : Calculer les variances sur les données brutes
    df_var = df.var().sort_values(ascending=False).values
    sum_df_var = df_var.sum()
    df_var_percent = (df_var / sum_df_var) * 100
    print("Pourcentage des variances des données brutes :")
    print(df_var_percent)
    
    # Normaliser les données brutes
    df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    df_var_normalized = df_normalized.var().sort_values(ascending=False).values
    sum_df_var_normalized = df_var_normalized.sum()
    df_var_normalized_percent = (df_var_normalized / sum_df_var_normalized) * 100
    print("Pourcentage des variances des données brutes normalisées :")
    print(df_var_normalized_percent)
    
    print("\n\n\n")
    
    # Normalisation des variances des données brutes
    variance_normalized_with_df_var = scaler.fit_transform(df_var.reshape(-1, 1)).flatten()
    sum_variance_normalized_with_df_var = variance_normalized_with_df_var.sum()
    variance_normalized_with_df_var_percent = (variance_normalized_with_df_var / sum_variance_normalized_with_df_var) * 100
    print("Pourcentage des variances des données brutes après normalisation :")
    print(variance_normalized_with_df_var_percent)
    
    # Normalisation des variances des données brutes normalisées
    variance_normalized_with_df_var_normalized = scaler.fit_transform(df_var_normalized.reshape(-1, 1)).flatten()
    sum_variance_normalized_with_df_var_normalized = variance_normalized_with_df_var_normalized.sum()
    variance_normalized_with_df_var_normalized_percent = (variance_normalized_with_df_var_normalized / sum_variance_normalized_with_df_var_normalized) * 100
    print("Pourcentage des variances des données brutes normalisées après normalisation :")
    print(variance_normalized_with_df_var_normalized_percent)
    
# Appel de la fonction avec le chemin du fichier
variance("C:/Users/said/Desktop/data_science/day05/Train_knight.csv")
