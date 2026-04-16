import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="moviesdb",
    user="postgres",
    password="postgres",
    port=5432
)

cursor = conn.cursor()

movies = pd.read_csv("data/movies.csv")

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
        (row["Title"], row["Year"], row["imdbID"])
    )

conn.commit()

cursor.close()
conn.close()

print("Dados inseridos no banco")