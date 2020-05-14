import os
import dotenv
import json
import requests

dotenv.load_dotenv()


class Movie:
    upc = None
    movie_name = None
    movie_year = None
    tmdb_id = None
    imdb_id = None
    runtime = None

    def __init__(self, upc, movie_name, movie_year):
        self.upc = upc
        self.movie_name = movie_name
        self.movie_year = movie_year
        self.find_movie_meta()

    def find_movie_meta(self):
        id_response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={os.getenv("TMDB_KEY")}'
                               f'&query={self.movie_name}&year={self.movie_year}')

        results = json.loads(id_response.content)['results']
        self.tmdb_id = results[0]['id']

        response = requests.get(f'https://api.themoviedb.org/3/movie/{self.tmdb_id}?api_key={os.getenv("TMDB_KEY")}')
        result = json.loads(response.content)
        self.imdb_id = result['imdb_id']
        self.runtime = result['runtime']

    def get_all_data(self):
        return self.movie_name, self.movie_year, self.tmdb_id, self.imdb_id, self.runtime
