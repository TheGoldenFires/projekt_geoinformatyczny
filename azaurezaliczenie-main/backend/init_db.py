import os
from pathlib import Path
from dotenv import load_dotenv
import pyodbc

# wczytanie zmiennych z .env
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT", "1433")

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={server},{port};DATABASE={database};"
    f"UID={username};PWD={password};Encrypt=yes;"
    "TrustServerCertificate=no;Connection Timeout=30;"
)

print("Łączenie z bazą danych...")
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

sql_path = Path(__file__).resolve().parents[1] / "db" / "db_init.sql"
with open(sql_path, "r", encoding="utf-8") as f:
    sql = f.read()

cursor.execute(sql)
conn.commit()
print("Tabele utworzone!")
cursor.close()
conn.close()
