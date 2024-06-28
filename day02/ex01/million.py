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
    SELECT event_time::date AS event_date, COUNT(DISTINCT user_id) AS buyer_count, SUM(price) AS total_price
    FROM {table_name}
    WHERE event_type = 'purchase' 
    GROUP BY event_date
    ORDER BY event_date;
    """

    cur.execute(query)
    data = cur.fetchall()
    print("query executed")
  
    df = pd.DataFrame(data, columns=['event_date', 'buyer_count', 'total_price'])
    df['event_date'] = pd.to_datetime(df['event_date'])  # Conversion en type datetime

    cur.close()
    conn.close()

    # Tracer la courbe avec Matplotlib pour le nombre d'acheteurs journaliers
    plt.plot(df['event_date'], df['buyer_count'], color='b')
    plt.ylabel('Number of buyers')
    plt.grid(True)

    # Customiser les étiquettes de l'axe X pour afficher uniquement Octobre, Novembre, Décembre, Janvier
    dates = pd.date_range(start='2022-10-01', end='2023-01-31', freq='MS').strftime("%b").tolist()
    plt.xticks(pd.date_range(start='2022-10-01', end='2023-01-31', freq='MS'), dates, rotation=45)
    
    plt.tight_layout()
    plt.show()

    #calcul depense moyenne par user dif
    print("right before expanse per different user")
    spent_per_customer = (df['total_price'].astype(float) * 0.8) / df['buyer_count']
    #plt.plot(df['event_date'], (df['total_price'].astype(float) * 0.8) / df['buyer_count'], color='b')
    plt.figure(figsize=(5,5))
    plt.fill_between(df['event_date'],spent_per_customer , color='lightblue', alpha=0.5)
    
    plt.ylabel('average spend/customer')
    plt.grid(True)
    dates = pd.date_range(start='2022-10-01', end='2023-01-31', freq='MS').strftime("%b").tolist()
    plt.xticks(pd.date_range(start='2022-10-01', end='2023-01-31', freq='MS'), dates, rotation=45)
    plt.yticks(range(0, int(spent_per_customer.max()) + 5, 5))
    plt.grid(True)
    plt.tight_layout()
    plt.show()


    # Calculer le revenu total par mois
    df['month'] = df['event_date'].dt.to_period('M')
    df['total_price'] = df['total_price'].astype(float)
    monthly_revenue = df.groupby('month')['total_price'].sum() / 1e6 * 0.8 # Diviser par 1e6 pour convertir en millions
    print("monthly revenue:", monthly_revenue)
   # Tracer le revenu total par mois sous forme de barres
    monthly_revenue.plot(kind='bar', color='skyblue')
    plt.xlabel('Mois')
    plt.ylabel('Revenu total (en millions)')
    plt.xticks(range(len(monthly_revenue)), ['Oct', 'Nov', 'Dec', 'Jan'], rotation=0)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

# Paramètres de la base de données
database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "foranalyse"

# Appel de la fonction
analyse_data(database, user, password, host, port, table_name)
