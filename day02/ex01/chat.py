import psycopg2
import matplotlib.pyplot as plt
from datetime import datetime

database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "tmp"  # Remplacez par le nom de votre table
column_name = "event_type"

def calculate_pourcent(database, user, password, host, port, table_name, column_name):
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cur = conn.cursor()

        cur.execute(f"""
            SELECT event_time, price FROM {table_name} WHERE {column_name} = 'cart';
            """)
        selection = cur.fetchall()
##compter le nombre d'evenement par date
        dates = [row[0] for row in selection]
        event_per_date = {}
        for date in dates:
            date_str = date.strftime('%Y-%m-%d')
            if date_str in event_per_date:
                event_per_date[date_str] += 1
            else:
                event_per_date[date_str] = 1
        print(event_per_date)

        # fig, ax = plt.subplots()
        # plt.show()

    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

calculate_pourcent(database, user, password, host, port, table_name, column_name)