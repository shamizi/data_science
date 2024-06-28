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
    SELECT event_time::date AS event_date, COUNT(DISTINCT user_id) AS buyer_count, SUM(price) AS prix
    FROM {table_name}
    WHERE event_type = 'purchase' 
    GROUP BY event_date
    ORDER BY event_date;
    """

    cur.execute(query)
    data = cur.fetchall()
    print("query executed")
    # Convertir les données en DataFrame Pandas
    df = pd.DataFrame(data, columns=['event_date', 'buyer_count', 'prix'])
    df['event_date'] = pd.to_datetime(df['event_date'])
    cur.close()
    conn.close()

    # Tracer la courbe avec Matplotlib
    plt.plot(df['event_date'], df['buyer_count'], marker=None)
    plt.ylabel('Number of customers')
    plt.grid(True)

    # Customiser les étiquettes de l'axe X pour afficher uniquement Octobre, Novembre, Décembre, Janvier
    dates = pd.date_range(start='2022-10-01', end='2023-01-31', freq='MS').strftime("%b").tolist()
    plt.xticks(pd.date_range(start='2022-10-01', end='2023-01-31', freq='MS'), dates, rotation=45)

    plt.tight_layout()
    plt.show()

    ##calcul recette par mois
    df['month'] = df['event_date'].dt.to_period('M')
    monthly_revenue = df.groupby('month')['prix'].sum() / 1e6
    print("monthly revenue :", monthly_revenue)

# Paramètres de la base de données
database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "foranalyse"

# Appel de la fonction
analyse_data(database, user, password, host, port, table_name)
