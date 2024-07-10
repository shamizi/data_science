import pandas as pd
import matplotlib.pyplot as plt

def point(file_path, file_path2):
    df = pd.read_csv(file_path2)
    df2 = pd.read_csv(file_path)

    jedi = df[df['knight'] == 'Jedi']
    sith = df[df['knight'] == 'Sith']

    fig, axes = plt.subplots(2,2)
    axes = axes.flatten()
    
#Sensitivity,Hability / Strength,Power,
    axes[0].scatter(jedi['Sensitivity'], jedi['Hability'],color='blue', marker='o', alpha=0.3)
    axes[0].scatter(sith['Sensitivity'], sith['Hability'],color='red', marker='o', alpha=0.3)
    axes[1].scatter(jedi['Strength'], jedi['Power'],color='blue', marker='o', alpha=0.3)
    axes[1].scatter(sith['Strength'], sith['Power'],color='red', marker='o', alpha=0.3)
    axes[2].scatter(df2['Sensitivity'], df2['Hability'],color='green', marker='o', alpha=0.3)
    axes[3].scatter(df2['Strength'], df2['Power'],color='green', marker='o', alpha=0.3)
    # for i, column in enumerate(df.columns):
    #     axes[i].hist(df[column], bins=40, color='green') 
    #     axes[i].set_title(column)
    #     axes[i].set_xlabel(column)
    #     axes[i].set_ylabel('Frequency')

    
    # # Supprimer les sous-graphiques vides
    # for i in range(len(df.columns), len(axes)):
    #     fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()

point("C:/Users/said/Desktop/data_science/day04/Test_knight.csv", "C:/Users/said/Desktop/data_science/day04/Train_knight.csv")