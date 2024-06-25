import pandas as pd
import psycopg2
from psycopg2 import sql, extras
import os

database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "pourtest"

folder_path = 'C:/Users/said/Desktop/data_science/ex03/customer'
csv_path = []
csv_name = []

for file in os.listdir(folder_path):
    if file.endswith('.csv'):
        csv_name.append(os.path.splitext(file)[0])
        csv_path.append(os.path.join(folder_path,file))

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    dbname=database,
    user=user,
    password=password,
    host=host,
    port=port
)

cur = conn.cursor()

for table_name, path in zip(csv_name, csv_path):
    cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}(
                event_time TIMESTAMP,
                event_type VARCHAR(255),
                product_id INT,
                price NUMERIC,
                user_id BIGINT,
                user_session TEXT
                )
                """)
    conn.commit()

    print(f"table {table_name} created")

    with open(path, 'r') as f:
        next(f)
        cur.copy_from(f, table_name, sep=',')
    conn.commit()
    print(f"data from {path} copied to {table_name}")

# cur.execute(f"SELECT * FROM {table_name}")
# print(cur.fetchone())
cur.close()
conn.close()
