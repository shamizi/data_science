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
table_name = "customers" #changer le nom

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
        cur.execute(f"""CREATE TEMPORARY TABLE tmp AS SELECT DISTINCT * FROM {table_name};
                CREATE TABLE IF NOT EXISTS clean(
                event_time TIMESTAMP,
                event_type VARCHAR(255),
                product_id INT,
                price FLOAT,
                user_id BIGINT,
                user_session TEXT
                );
                    INSERT INTO clean SELECT * FROM tmp;""")
        conn.commit()
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
