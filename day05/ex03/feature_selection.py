from statsmodels.stats.outliers_influence import variance_inflation_factor 
from statsmodels.tools.tools import add_constant
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd

def vif(path_file):
    train = pd.read_csv(path_file)
    features = train.iloc[:, :-1]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    df = pd.DataFrame(scaled_features, columns=features.columns)

    vif = pd.DataFrame()
    vif["Feature"] = df.columns
    vif["VIF"] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
    vif["tolerance"] = 1 / vif['VIF']
    
    print(vif)

vif("C:/Users/said/Desktop/data_science/day05/Train_knight.csv")