import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

def heatmap(path_file, pathfile2):
    train = pd.read_csv(path_file)
    test = pd.read_csv(pathfile2)
    label_encoder = LabelEncoder()

    df = pd.DataFrame(train)
    df['knight'] = label_encoder.fit_transform(df["knight"])
    corelation = df.corr()
    sns.heatmap(corelation)
    plt.show()
heatmap("C:/Users/said/Desktop/data_science/day05/Train_knight.csv","C:/Users/said/Desktop/data_science/day05/Test_knight.csv")