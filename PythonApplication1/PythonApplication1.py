import pymysql
import pandas as pd
import json
from sqlalchemy import create_engine

# Leggi i dati dal file JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# Crea un motore SQLAlchemy per il database
engine = create_engine('mysql+pymysql://root:Ciao1234@localhost/blog1')

# Per ogni chiave nel dizionario JSON, crea una tabella e popolala con i dati corrispondenti
for table, records in data.items():
    df = pd.DataFrame(records)
    df.to_sql(table, engine, if_exists='replace', index=False)

print("Tabelle create e popolate con successo.")


