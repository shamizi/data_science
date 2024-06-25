import psycopg2
from psycopg2 import sql
import matplotlib.pyplot as plt

database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "pourtest"  # Remplacez par le nom de votre table
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
        print("connected")
        cur.execute(f"""SELECT COUNT(*) FROM {table_name};""")
        nb_event = cur.fetchone()[0] #nb d'event
        print(nb_event)

        cur.execute(f"""
            SELECT {column_name}, COUNT(*)
            FROM {table_name}
            GROUP BY {column_name}
            ORDER BY COUNT(*) DESC
            """)
        dif_event = cur.fetchall()
        print(dif_event)

        event_percentage = [(event_type, count, (count / nb_event) * 100) for event_type, count in dif_event]
        #print("% :", event_percentage) #name / nombre d'occurence / %
        labels = [event[0] for event in event_percentage]
        percentages = [event[2] for event in event_percentage]
        ax = plt.subplots()
        ax.pie(percentages, labels=labels, autopct='%1.1f%%')
        plt.show()

    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

calculate_pourcent(database, user, password, host, port, table_name, column_name)