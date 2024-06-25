import pandas as pd
import psycopg2
from psycopg2 import sql, extras

csv_path = 'data_2022_dec.csv'
database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "data_2022_dec"

df = pd.read_csv(csv_path)

conn = psycopg2.connect(
    dbname=database,
    user=user,
    password=password,
    host=host,
    port=port
)
print("3")

cur = conn.cursor()
print("4")

columns = df.columns
create_table_query = sql.SQL(
    "CREATE TABLE IF NOT EXISTS {} ({})"
).format(
    sql.Identifier(table_name),
    sql.SQL(', ').join(
        sql.SQL("{} {}").format(
            sql.Identifier(col),
            sql.SQL("TEXT")  # Vous pouvez ajuster les types de données ici
        ) for col in columns
    )
)
print("5")


# Exécution de la requête de création de table
cur.execute(create_table_query)
conn.commit()
print("6")

# Insertion des données dans la table
insert_query = sql.SQL(
    "INSERT INTO {} ({}) VALUES %s"
).format(
    sql.Identifier(table_name),
    sql.SQL(', ').join(map(sql.Identifier, columns))
)

data = [tuple(row) for row in df.to_numpy()]
extras.execute_batch(cur, insert_query, data)

print("7")

# Commit et fermeture de la connexion
conn.commit()
cur.close()
conn.close()

print("Table created and data inserted successfully.")