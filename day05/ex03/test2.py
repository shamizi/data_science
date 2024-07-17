import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler
from statsmodels.tools.tools import add_constant
def vif(path_file, vif_threshold=5):
    # Step 1: Read data from CSV
    df = pd.read_csv(path_file)
    
    # Step 2: Identify predictor variables
    X = add_constant(df)
    X = df.drop(columns=['knight'])  # Replace with your response variable column name
    
    # Step 3: Standardize the predictor variables
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Step 4: Calculate VIF
    vif_values = [variance_inflation_factor(X_scaled, i) for i in range(X_scaled.shape[1])]
    tolerance_values = [1 / vif for vif in vif_values]
    
    # Step 5: Create DataFrame to display VIF and Tolerance
    vif_df = pd.DataFrame({'VIF': vif_values, 'TOLERANCE': tolerance_values}, index=X.columns)
    
    # Step 6: Display the result
    print("VIF and Tolerance:")
    print(vif_df)
    
    # Step 7: Iteratively drop variables with high VIF until all VIFs are below the threshold
    while vif_df['VIF'].max() > vif_threshold:
        # Identify the variable with the highest VIF
        max_vif_feature = vif_df['VIF'].idxmax()
        
        # Drop the variable with the highest VIF
        X = X.drop(columns=[max_vif_feature])
        
        # Re-calculate VIF
        X_scaled = scaler.fit_transform(X)
        vif_values = [variance_inflation_factor(X_scaled, i) for i in range(X_scaled.shape[1])]
        tolerance_values = [1 / vif for vif in vif_values]
        
        # Update DataFrame
        vif_df = pd.DataFrame({'VIF': vif_values, 'TOLERANCE': tolerance_values}, index=X.columns)
        
        # Display updated result
        print("\nAfter dropping", max_vif_feature)
        print(vif_df)
    
    # Step 8: Return the selected features
    selected_features = vif_df.index.tolist()
    print(selected_features)

# Exemple d'utilisation
vif("C:/Users/said/Desktop/data_science/day05/Train_knight.csv")

