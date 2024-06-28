import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
from collections import defaultdict
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
    query = f"""
    SELECT user_id, event_time, event_type, price
    FROM {table_name}
    ORDER BY event_time;
    """

    cur.execute(query)
    data = cur.fetchall()
    print("query executed")

    daily_sales = defaultdict(float)
    unique_customers = defaultdict(set)
    for user_id, event_time, event_type, price in data:
        if event_type == 'purchase':
            date_str = event_time.strftime('%Y-%m-%d')
            daily_sales[date_str] += price
            unique_customers[date_str].add(user_id)
    
    dates = list(daily_sales.keys())
    
    average_spend_per_customer = [daily_sales[date] * 0.8 / len(unique_customers[date])
                                  for date in dates]
    
    plt.figure(figsize=(10, 6))
    plt.plot(dates, average_spend_per_customer, color='blue', alpha=0.3)
    plt.fill_between(dates, average_spend_per_customer, color='blue', alpha=0.3)
    plt.ylabel("Average Spend/Customer in A")
    tick_positions = [0, len(dates) // 4, 2 * len(dates) // 4, 3 * len(dates) // 4]
    tick_labels = ["Oct", "Nov", "Dec", "Jan"]
    plt.xticks(tick_positions, tick_labels)
    plt.yticks(np.arange(0, max(average_spend_per_customer), 5))
    plt.xlim(dates[0], dates[-1])
    plt.ylim(0)
    plt.show()


database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "foranalyse"

# Appel de la fonction
analyse_data(database, user, password, host, port, table_name)
