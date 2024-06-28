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
    SELECT DISTINCT price
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
    second_quartile = df['price'].quantile(0.5)  # Correspond à la médiane
    third_quartile = df['price'].quantile(0.75)

    print(f"count {count}") #parenthese a count surement
    print(f"mean {mean_price:.6f}")
    print(f"std {std_price:.6f}")
    print(f"min {min_price:.6f}")
    print(f"25% {first_quartile:.6f}")
    print(f"50% {second_quartile:.6f}")
    print(f"75% {third_quartile:.6f}")
    print(f"max {max_price:.6f}")


database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "foranalyse"

# Appel de la fonction
analyse_data(database, user, password, host, port, table_name)
