import pandas as pd
import psycopg2
from psycopg2 import sql, extras
import os

database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "items"

folder_path = 'C:/Users/said/Desktop/data_science/ex04/item'
csv_path = []

for file in os.listdir(folder_path):
    if file.endswith('.csv'):
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


cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}(
            product_id INT NULL,
            category_id NUMERIC NULL,
            category_code TEXT,
            brand TEXT
            )
            """)
conn.commit()

print(f"table {table_name} created")

with open(csv_path[0], 'r') as f:
    next(f)
    cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER NULL AS ''", f)
conn.commit()
print(f"data from {csv_path} copied to {table_name}")

# cur.execute(f"SELECT * FROM {table_name}")
# print(cur.fetchone())
cur.close()
conn.close()
