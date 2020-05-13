from tmdbv3api import TMDb


class APIData:
    movie_name = None
    api_key = None

    def __init__(self, movie_name):
        self.tmdb = TMDb()
        self.tmdb.api_key = self.api_key
        self.movie_name = movie_name
        self.find_movie_meta()

    def get_api_key(self):
        f = open('api_key.txt')
        line = f.readline()
        self.api_key = line[0]

    def find_movie_meta(self):
        results = movie.search(self.movie_name)

        for res in results:
            print(res.id)
            print(res.title)

    def get_all_data(self):
        return self.movie_name