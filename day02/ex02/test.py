import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import numpy as np

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
    query_prices = f"""
    SELECT price
    FROM {table_name}
    WHERE event_type = 'purchase' 
    """
    cur.execute(query_prices)
    data_prices = cur.fetchall()
    print("query for prices executed")

    df_prices = pd.DataFrame(data_prices, columns=['price'])
    df_prices['price'] = df_prices['price'].astype(float)

    count = df_prices['price'].count()
    mean_price = df_prices['price'].mean()
    std_price = df_prices['price'].std()
    min_price = df_prices['price'].min()
    max_price = df_prices['price'].max()
    first_quartile = df_prices['price'].quantile(0.25)
    second_quartile = df_prices['price'].quantile(0.5)  # Correspond à la médiane
    third_quartile = df_prices['price'].quantile(0.75)

    print(f"count {count:.6f}")
    print(f"mean {mean_price:.6f}")
    print(f"std {std_price:.6f}")
    print(f"min {min_price:.6f}")
    print(f"25% {first_quartile:.6f}")
    print(f"50% {second_quartile:.6f}")
    print(f"75% {third_quartile:.6f}")
    print(f"max {max_price:.6f}")

    # Requête SQL pour récupérer le prix moyen d'achat par utilisateur
    query_avg_price_per_user = f"""
    SELECT user_id, AVG(price) as avg_price
    FROM {table_name}
    WHERE event_type = 'cart'
    GROUP BY user_id
    HAVING AVG(price) BETWEEN 26 AND 43
    """
    cur.execute(query_avg_price_per_user)
    data_avg_price_per_user = cur.fetchall()
    print("query for avg price per user executed")

    df_avg_price_per_user = pd.DataFrame(data_avg_price_per_user, columns=['user_id', 'avg_price'])
    df_avg_price_per_user['avg_price'] = df_avg_price_per_user['avg_price'].astype(float)

    count_avg = df_avg_price_per_user['avg_price'].count()
    mean_avg_price = df_avg_price_per_user['avg_price'].mean()
    std_avg_price = df_avg_price_per_user['avg_price'].std()
    min_avg_price = df_avg_price_per_user['avg_price'].min()
    max_avg_price = df_avg_price_per_user['avg_price'].max()
    first_quartile_avg = df_avg_price_per_user['avg_price'].quantile(0.25)
    second_quartile_avg = df_avg_price_per_user['avg_price'].quantile(0.5)  # Correspond à la médiane
    third_quartile_avg = df_avg_price_per_user['avg_price'].quantile(0.75)

    print(f"count_avg {count_avg:.6f}")
    print(f"mean_avg {mean_avg_price:.6f}")
    print(f"std_avg {std_avg_price:.6f}")
    print(f"min_avg {min_avg_price:.6f}")
    print(f"25% avg {first_quartile_avg:.6f}")
    print(f"50% avg {second_quartile_avg:.6f}")
    print(f"75% avg {third_quartile_avg:.6f}")
    print(f"max_avg {max_avg_price:.6f}")

    cur.close()
    conn.close()

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(21, 6))
    boxes = ax1.boxplot(df_prices['price'], vert=False, widths=0.5, notch=True,
                        boxprops=dict(facecolor='lightgray', edgecolor='none'),
                        flierprops=dict(marker='D', markersize=8, markerfacecolor='lightgray', markeredgecolor='none'),
                        patch_artist=True)
    ax1.set_yticks([])
    ax1.set_xlabel("Price")
    ax1.set_title("Full Box Plot")

    boxprops = dict(facecolor='green', edgecolor='black')
    medianprops = dict(linestyle='-', linewidth=2, color='black')
    ax2.boxplot(df_prices['price'], vert=False, widths=0.5, notch=True,
                boxprops=boxprops, medianprops=medianprops, showfliers=False,
                patch_artist=True)
    ax2.set_yticks([])
    ax2.set_xlabel("Price")
    ax2.set_title("Interquartile range (IQR)")

    avg_cart_prices = df_avg_price_per_user['avg_price']
    ax3.boxplot(avg_cart_prices, vert=False, widths=0.5, notch=True,
                boxprops=dict(facecolor='lightblue', edgecolor='black'),
                flierprops=dict(marker='D', markersize=8, markerfacecolor='lightgray', markeredgecolor='none'),
                patch_artist=True, whis=0.2)
    ax3.set_xticks(np.arange(int(min(avg_cart_prices)), int(max(avg_cart_prices)) + 1, step=2))
    ax3.set_xlim(min(avg_cart_prices) - 1, max(avg_cart_prices) + 1)
    ax3.set_yticks([])
    ax3.set_xlabel("Average Price per User")
    ax3.set_title("Box Plot of Average Purchase Price per User")

    plt.tight_layout()
    plt.show()

database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "foranalyse"

# Appel de la fonction
analyse_data(database, user, password, host, port, table_name)
