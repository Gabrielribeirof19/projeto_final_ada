import psycopg2
import pandas as pd
import os

conn = psycopg2.connect(
    host= "localhost",
    database="moviesdb",
    user="postgres",
    password="postgres",
    port=5432
)

print("📂 CWD:", os.getcwd())
print("📁 Files:", os.listdir())

movies = pd.read_csv("movies.csv")

print(f"📊 Linhas carregadas do CSV: {len(movies)}")
print(movies.head())

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title TEXT,
    year TEXT,
    imdb_id TEXT
)
""")

print("\n" + "="*60)
print("📊 DADOS INSERIDOS NO BANCO")
print("="*60)

print(f"{'TITLE':40} {'YEAR':6} {'IMDB_ID'}")
print("-"*60)

inserted = 0

for _, row in movies.iterrows():
    cursor.execute(
        "INSERT INTO movies (title, year, imdb_id) VALUES (%s,%s,%s)",
        (row["title"], row["year"], row["movie_id"])  # mapeamento correto
    )

    inserted += 1

    print(f"{row['title'][:38]:40} {row['year']:<6} {row['movie_id']}")

conn.commit()

print("-"*60)
print(f"✔️ Total inserido: {inserted}")
print("="*60)

cursor.execute("SELECT COUNT(*) FROM movies;")
total = cursor.fetchone()[0]

print(f"📦 TOTAL NO BANCO: {total}")
print("="*60)

cursor.close()
conn.close()

print("🚀 Dados inseridos no banco com sucesso")