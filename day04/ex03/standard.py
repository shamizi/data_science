import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder

def standar(file_path, file_path2):
    df = pd.read_csv(file_path2)
    df2 = pd.read_csv(file_path)
#encoder la colonne knight vers valeur numérique
    label_encoder = LabelEncoder()
    df['knight'] = label_encoder.fit_transform(df['knight'])
#standardiser les data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df.drop(columns=['knight']))
    scaled_data2 = scaler.fit_transform(df2)

    df_scaled = pd.DataFrame(scaled_data, columns=df.columns[:-1])
    df_scaled2 = pd.DataFrame(scaled_data2, columns=df2.columns)
    
    df_scaled['knight'] = df['knight'].values
    print(df_scaled)
    print(df_scaled2)


    jedi = df_scaled[df_scaled['knight'] == 0]
    sith = df_scaled[df_scaled['knight'] == 1]

    fig, axes = plt.subplots(2,2)
    axes = axes.flatten()
    
#Sensitivity,Hability / Strength,Power,
    axes[0].scatter(jedi['Sensitivity'], jedi['Hability'],color='blue', marker='o', alpha=0.3)
    axes[0].scatter(sith['Sensitivity'], sith['Hability'],color='red', marker='o', alpha=0.3)
    axes[1].scatter(jedi['Strength'], jedi['Power'],color='blue', marker='o', alpha=0.3)
    axes[1].scatter(sith['Strength'], sith['Power'],color='red', marker='o', alpha=0.3)
    axes[2].scatter(df_scaled2['Sensitivity'], df_scaled2['Hability'],color='green', marker='o', alpha=0.3)
    axes[3].scatter(df_scaled2['Strength'], df_scaled2['Power'],color='green', marker='o', alpha=0.3)

    plt.tight_layout()
    plt.show()

standar("C:/Users/said/Desktop/data_science/day04/Test_knight.csv", "C:/Users/said/Desktop/data_science/day04/Train_knight.csv")