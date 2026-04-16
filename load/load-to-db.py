import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="postgres",
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

for _, row in movies.iterrows():
    cursor.execute(
        "INSERT INTO movies (title, year, imdb_id) VALUES (%s,%s,%s)",
        (row["title"], row["year"], row["imdb_id"])
    )

conn.commit()
cursor.close()
conn.close()

print("Dados inseridos no banco")