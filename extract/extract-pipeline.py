import pandas as pd
import requests
import os

API_KEY = os.getenv("OMDB_API_KEY")

print (f"Chave da API OMDb: {API_KEY}")

url = f"http://www.omdbapi.com/?i=tt3896198&apikey={API_KEY}"

response = requests.get(url)
movie = response.json()

print(movie)

if movie.get("Response") == "False":
    raise Exception(f"Erro da API OMDb: {movie.get('Error')}")

movies = pd.DataFrame([movie])

movies = movies.rename(columns={
    "Title": "title",
    "Year": "year",
    "imdbID": "imdb_id"
})

os.makedirs("data", exist_ok=True)

movies.to_csv("data/movies.csv", index=False)

print("CSV de filmes gerado")