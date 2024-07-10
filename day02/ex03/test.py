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
    print("Connected to database")
    
    # Requête SQL pour récupérer les données d'achat
    query = f"""
    SELECT user_id, COUNT(*) AS order_count
    FROM {table_name}
    WHERE event_type = 'purchase'
    GROUP BY user_id
    """
    
    cur.execute(query)
    data = cur.fetchall()
    print("Query executed")
    
    # Fermeture de la connexion et du curseur
    cur.close()
    conn.close()
    
    # Création d'un DataFrame Pandas avec les résultats de la requête
    df = pd.DataFrame(data, columns=['user_id', 'order_count'])
    
    # Filtrer les données pour exclure les utilisateurs avec plus de 40 commandes
    df = df[df['order_count'] <= 40]
    # Titres et labels
   # plt.hist(df['order_count'],bins=5)
    plt.hist(df['order_count'], bins=5, color='skyblue', edgecolor='white', align='mid')
    plt.xlabel('Frequency')
    plt.ylabel('Customers')
    plt.xticks(range(0, 31, 10))
    plt.yticks(range(0, 60001, 10000))
    plt.grid(True)
    # Affichage du graphique
    plt.tight_layout()
    plt.show()

# Détails de connexion à la base de données
database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "customers"

# Appel de la fonction d'analyse
analyse_data(database, user, password, host, port, table_name)
