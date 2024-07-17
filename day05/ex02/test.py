### tester de normaliser puis de standardiser 
### bien oublier de transormer en %

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np

def variance(path_file):
    train = pd.read_csv(path_file)
    label_encoder = LabelEncoder()
    scaler = MinMaxScaler()
    scaler2 = StandardScaler() #meme variance pour tout
    df = pd.DataFrame(train)
   # df = df.drop(columns='knight')
   # df['knight'] = label_encoder.fit_transform(df["knight"])
    
    
    numeric_columns = train.select_dtypes(include=[np.number])
    numeric_columns_normalized = pd.DataFrame(scaler.fit_transform(numeric_columns), columns=numeric_columns.columns)
    # Calculer la variance de chaque colonne numérique
    variances = numeric_columns_normalized.var().sort_values(ascending=False).values
    sum_var = variances.sum()
    variances_percent = (variances / sum_var) * 100
    print(variances_percent)
    variances_normalized = scaler.fit_transform(variances.reshape(-1, 1)).flatten()
    variances_normalized_percent = (variances_normalized / variances_normalized.sum()) * 100
    print(variances_normalized_percent)
    # print("Variances de chaque colonne :")
    # print(variances)
    # print("variance normaliser :")
    # print(variances_normalized)
    print("\n\n")
    #############################################
    df_var = df.var().sort_values(ascending=False).values
    df_normalised = pd.DataFrame(scaler.fit_transform(df))
    df_var_normalised = df_normalised.var().sort_values(ascending=False).values
    # print("df_var :", df_var)
    # print("df_var_normalised", df_var_normalised)
    print("\n\n\n")
    variance_normaliser_avec_dfvar = scaler.fit_transform(df_var.reshape(-1, 1)).flatten()
    variance_normaliser_avec_dfvar_normalised = scaler.fit_transform(df_var_normalised.reshape(-1, 1)).flatten()

    ########################
    variance_normaliser_avec_dfvar_percent = (variance_normaliser_avec_dfvar / variance_normaliser_avec_dfvar.sum()) * 100
    print("variance normaliser avec dfvar percent", variance_normaliser_avec_dfvar_percent)
    variance_normaliser_avec_dfvar_normalised_percent = (variance_normaliser_avec_dfvar_normalised / variance_normaliser_avec_dfvar_normalised.sum()) * 100
    print("variance normaliser avec dfvar normalised percent", variance_normaliser_avec_dfvar_normalised_percent)

    #######################
    # print("normaliser avec df var", variance_normaliser_avec_dfvar)
    # #3.97 e-1 * 100 pour pourcentage c'est crédible
    # print("normaliser avec df var normalised", variance_normaliser_avec_dfvar_normalised)
    



variance("C:/Users/said/Desktop/data_science/day05/Test_knight.csv")