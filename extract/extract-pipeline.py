import pandas as pd
import requests
import os

API_KEY = os.getenv("OMDB_API_KEY")

url = f"http://www.omdbapi.com/?i=tt3896198&apikey={API_KEY}"

response = requests.get(url)
movie = response.json()

movies = pd.DataFrame([movie])

movies = movies.rename(columns={
    "Title": "title",
    "Year": "year",
    "imdbID": "imdb_id"
})

movies.to_csv("data/movies.csv", index=False)

print("CSV de filmes gerado")