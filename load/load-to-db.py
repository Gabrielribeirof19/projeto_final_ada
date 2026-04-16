import pandas as pd
import psycopg2

movies = pd.read_csv("data/movies.csv")

conn = psycopg2.connect(
    host="localhost",
    database="moviesdb",
    user="postgres",
    password="postgres",
    port=5432
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title TEXT,
    year TEXT,
    imdb_id TEXT
)
""")
print(movies.columns)
for _, row in movies.iterrows():

    cursor.execute(
        "INSERT INTO movies (title, year, imdb_id) VALUES (%s,%s,%s)",
        (row["title"], row["year"], row["imdb_id"])
    )

conn.commit()

cursor.close()
conn.close()

print("Dados inseridos no banco")