import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

def analyse_data(database, user, password, host, port, table_name):
    # Connexion à la base de données PostgreSQL
    conn = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cur = conn.cursor()
    print("connected")
    
    # Requête SQL pour récupérer les achats de la période spécifiée
    query = f"""
    SELECT price
    FROM {table_name}
    WHERE event_type = 'purchase' 
    """

    cur.execute(query)
    data = cur.fetchall()
    print("query executed")

    df = pd.DataFrame(data, columns=['price'])
    df['price'] = df['price'].astype(float)
    count = df['price'].count()
    mean_price = df['price'].mean()
    std_price = df['price'].std()
    min_price = df['price'].min()
    max_price = df['price'].max()
    first_quartile = df['price'].quantile(0.25)
    second_quartile = df['price'].median()  # Correspond à la médiane
    third_quartile = df['price'].quantile(0.75)

    print(f"count {count:.6f}") #parenthese a count surement
    print(f"mean {mean_price:.6f}")
    print(f"std {std_price:.6f}")
    print(f"min {min_price:.6f}")
    print(f"25% {first_quartile:.6f}")
    print(f"50% {second_quartile:.6f}")
    print(f"75% {third_quartile:.6f}")
    print(f"max {max_price:.6f}")
    # plt.boxplot(
    #     df['price'],
    #     vert=False,
    #     patch_artist=True,
    #     boxprops=dict(facecolor='lightblue', linewidth=2),  # Épaisseur de la boîte
    #     whiskerprops=dict(linewidth=2),  # Épaisseur des whiskers
    #     capprops=dict(linewidth=2),  # Épaisseur des capuchons
    #     medianprops=dict(linewidth=2, color='red')  # Épaisseur de la ligne médiane
    # )
    # plt.xlabel('price')
    # plt.grid(True)
    # plt.show()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    boxes = ax1.boxplot(df['price'], vert=False, widths=0.5, notch=True,
                        boxprops=dict(facecolor='lightgray', edgecolor='none'),
                        flierprops=dict(marker='D', markersize=8, markerfacecolor='lightgray', markeredgecolor='none'),
                        patch_artist=True)
    ax1.set_yticks([])
    ax1.set_xlabel("Price")
    ax1.set_title("Full Box Plot")

    boxprops = dict(facecolor='green', edgecolor='black')
    medianprops = dict(linestyle='-', linewidth=2, color='black')
    ax2.boxplot(df['price'], vert=False, widths=0.5, notch=True,
                boxprops=boxprops, medianprops=medianprops, showfliers=False,
                patch_artist=True)
    ax2.set_yticks([])
    ax2.set_xlabel("Price")
    ax2.set_title("Interquartile range (IQR)")
#pour boite a moustache 2 afficher jusqu'a 12 et 3eme quartile pas la bonne valeur
    plt.tight_layout()
    plt.show()

database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "customers"

# Appel de la fonction
analyse_data(database, user, password, host, port, table_name)
