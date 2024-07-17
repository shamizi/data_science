import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from statsmodels.tools.tools import add_constant

def calculate_vif(X):
    vif_data = pd.DataFrame()
    vif_data['Variable'] = X.columns
    vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif_data['Tolerance'] = 1 / vif_data['VIF']
    return vif_data

def vif_analysis(path_file):
    # Load the dataset
    data = pd.read_csv(path_file)
    scaler = StandardScaler()
    scaler2 = MinMaxScaler()

    # Extract predictor variables (excluding the target variable)
    X = data.drop('knight', axis=1)
    
    # Standardize the predictor variables
    scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(scaled, columns=X.columns)

    # Calculate VIF for each predictor variable
    vif_data = calculate_vif(X_scaled)
    print("Initial VIF values:\n", vif_data)
    
    # Iteratively remove variables with high VIF
    while vif_data['VIF'].max() > 5:
        # Find the variable with the highest VIF
        max_vif_var = vif_data.loc[vif_data['VIF'].idxmax(), 'Variable']
        print(f"\nRemoving variable '{max_vif_var}' with VIF {vif_data['VIF'].max()}")
        
        # Drop this variable
        X_scaled = X_scaled.drop(columns=[max_vif_var])
        
        # Recalculate VIF
        vif_data = calculate_vif(X_scaled)
        print(vif_data)
    
    print("\nFinal set of variables with acceptable VIF values:\n", vif_data)

# Example usage
vif_analysis("C:/Users/said/Desktop/data_science/day05/Train_knight.csv")
