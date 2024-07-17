import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler, LabelEncoder
from statsmodels.tools.tools import add_constant
def vif(path_file):

# Load the dataset
    data = pd.read_csv(path_file)
    scaler = StandardScaler()
    label_encoder = LabelEncoder()
    #data['knight'] = label_encoder.fit_transform(data["knight"])

# Extract predictor variables (excluding the target variable)
    y = data.drop('knight', axis=1)
    y = add_constant(y)
    scaled = scaler.fit_transform(y)
    X = pd.DataFrame(scaled, columns=y.columns)

# Calculate VIF for each predictor variable
    vif = pd.DataFrame()
    vif['Variable'] = X.columns
    vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif['Tolerance'] = 1 / vif['VIF']
# Display variables with VIF > 5
    print(vif[vif['VIF'] > 5])
    print("\nlow tolerance")
    print(vif[vif['Tolerance'] < 0.2])

    print("test")
    print(vif.sort_values('Tolerance', ascending=False))

# Example usage
vif("C:/Users/said/Desktop/data_science/day05/Train_knight.csv")

# import pandas as pd
# from statsmodels.stats.outliers_influence import variance_inflation_factor
# from sklearn.preprocessing import LabelEncoder

# def vif(path_file):
#     # Lire le fichier CSV
#     train = pd.read_csv(path_file)
    
#     # Encoder la colonne de chaînes de caractères
#     label_encoder = LabelEncoder()
#     train['knight'] = label_encoder.fit_transform(train["knight"])
#     #train = train.drop(columns='knight')
#     #train = train.dropna(axis=1)
#     # Créer le DataFrame avec constante
#     train_with_const = train
    
#     # Calculer le VIF pour chaque variable
#     vif_data = pd.DataFrame()
#     vif_data["feature"] = train_with_const.columns
#     vif_data["VIF"] = [variance_inflation_factor(train_with_const.values, i) for i in range(train_with_const.shape[1])]
    
#     print("Initial VIF values:")
#     print(vif_data)
    
#     # Liste pour stocker les variables supprimées
#     removed_features = []
    
#     # Supprimer les variables avec un VIF supérieur à 5
#     while vif_data['VIF'].max() > 5:
#         #to_remove = vif_data.loc[vif_data["VIF"] > 5, 'feature'].iloc[0]
#         to_remove = vif_data['VIF'].idxmax()
#         removed_features.append({
#             'feature': to_remove,
#             'VIF': vif_data.loc[vif_data['feature'] == to_remove, 'VIF'].values[0]
#         })
#         train_with_const = train_with_const.drop(columns=[to_remove])
#         vif_data = pd.DataFrame()
#         vif_data["feature"] = train_with_const.columns
#         vif_data["VIF"] = [variance_inflation_factor(train_with_const.values, i) for i in range(train_with_const.shape[1])]
    
#     # Convertir la liste en DataFrame final des variables retirées
#     removed_features_df = pd.DataFrame(removed_features)
    
#     print("Removed features to achieve VIF <= 5:")
#     print(removed_features_df)
    
# # Exemple d'utilisation
# vif("C:/Users/said/Desktop/data_science/day05/Train_knight.csv")
