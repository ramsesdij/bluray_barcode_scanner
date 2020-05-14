import os
import dotenv
import pymysql.cursors

dotenv.load_dotenv()


class MovieDatabase:
    def __init__(self):
        self.connection = pymysql.connect(host=os.getenv("DB_HOST"),
                                     user=os.getenv("DB_USER"),
                                     password=os.getenv("DB_PASSWORD"),
                                     db=os.getenv("DB_NAME"),
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

    def add_movie(self, movie):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `movies` (`movie_name`, `movie_year`, `pub_nation`, `duration_minutes`, `tmdb_id`, `imdb_id`, `upc`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s)"

                cursor.execute(sql, (movie['movie_name'], movie['movie_year'], movie['pub_nation'],
                                     int(movie['runtime']), movie['tmdb_id'], movie['imdb_id'], movie['upc']))

            self.connection.commit()
            print("ADDED MOVIE TO DATABASE")
        finally:
            self.connection.close()

    def display_all_movies(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT `*` FROM `movies`"
                cursor.execute(sql)

                return cursor.fetchall()
        finally:
            self.connection.close()

    def search_movie_by_name(self, query):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT `*` FROM `movies` WHERE `movie_name` LIKE CONCAT('%', %s, '%')"
                cursor.execute(sql, query)

                return cursor.fetchall()
        finally:
            self.connection.close()
