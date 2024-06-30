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

def fusion(database, user, password, host, port, table_name):
    logging.info("Début de la création de la table temporaire et de la fusion des données")
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

        # Ajout des colonnes de la table 'item' dans 'tmp'
        # Assurez-vous que les colonnes de 'item' n'existent pas déjà dans 'tmp'

        cur.execute(sql.SQL("""
            ALTER TABLE {table}
            ADD COLUMN IF NOT EXISTS category_id NUMERIC NULL,
            ADD COLUMN IF NOT EXISTS category_code TEXT,
            ADD COLUMN IF NOT EXISTS brand TEXT
        """).format(
            table=sql.Identifier(table_name)
        ))
        conn.commit()

        logging.info("Colonnes ajoutées avec succès à la table temporaire")

        # Mise à jour de la table 'tmp' avec les données de la table 'item'
        cur.execute(sql.SQL("""
            UPDATE {table}
            SET category_id = items.category_id,
                category_code = items.category_code,
                brand = items.brand
            FROM items
            WHERE {table}.product_id = items.product_id
        """).format(
            table=sql.Identifier(table_name)
        ))
        conn.commit()

        logging.info("Données fusionnées avec succès dans la table temporaire")

    except Exception as e:
        logging.error(f"Erreur lors de la fusion des données : {e}")
        conn.rollback()  # Rollback en cas d'erreur
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        logging.info("Connexion à la base de données fermée")

fusion(database, user, password, host, port, table_name)
