import psycopg2
from psycopg2 import sql
import logging

# Configuration de la journalisation
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

database = "piscineds"
user = "shamizi"
password = "mysecretpassword"
host = "localhost"
port = "5432"
table_name = "data_2022_oct" #changer le nom

def delete_duplicate(database, user, password, host, port, table_name):
    logging.info("Début de la suppression des doublons")
    try:
        # Connexion à la base de données
        logging.info("Connexion à la base de données")
        conn = psycopg2.connect(
            dbname=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cur = conn.cursor()

        cur.execute(f"""CREATE TABLE pourtest AS SELECT DISTINCT * FROM {table_name};""")
        conn.commit()
        tables_to_insert = ["data_2022_nov", "data_2022_dec", "data_2023_jan"]
        for table in tables_to_insert:
            cur.execute(f"""INSERT INTO pourtest (SELECT DISTINCT * FROM {table});""")
            conn.commit()
            print(f"Données de {table} insérées dans pourtest")

        conn.commit()
        # cur.execute(f"""CREATE TEMPORARY TABLE tmp AS SELECT DISTINCT * FROM {table_name};
        #             TRUNCATE {table_name};
        #             INSERT INTO {table_name} SELECT * FROM tmp;""")
        # conn.commit()
        logging.info("Suppression des doublons terminée avec succès.")
    except Exception as e:
        logging.error(f"Erreur lors de la suppression des doublons : {e}")
        conn.rollback()  # Rollback en cas d'erreur
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        logging.info("Connexion à la base de données fermée")

delete_duplicate(database, user, password, host, port, table_name)
