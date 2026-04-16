import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="moviesdb",
    user="postgres",
    password="postgres",
    port=5432
)

movies = pd.read_csv("data/movies.csv")

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
        (row["title"], row["year"], row["imdb_id"])
    )

    inserted += 1

    # imprime linha formatada (limita tamanho do título)
    print(f"{row['title'][:38]:40} {row['year']:<6} {row['imdb_id']}")

conn.commit()

print("-"*60)
print(f"✔️ Total inserido: {inserted}")
print("="*60 + "\n")

cursor.execute("SELECT COUNT(*) FROM movies;")
total = cursor.fetchone()[0]

print(f"📦 TOTAL NO BANCO: {total}")
print("="*60)

conn.commit()
cursor.close()
conn.close()

print("Dados inseridos no banco")