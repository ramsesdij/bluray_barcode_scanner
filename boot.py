from flask import Flask, jsonify, request
from src.scrape_data import ScrapeData
from src.api_data import Movie
from src.rds_client import MovieDatabase

app = Flask(__name__)


@app.route('/analyse_barcode')
def analyse_barcode():
    upc = request.args.get('upc')
    scrape_data = ScrapeData(upc)
    movie_name, movie_year, pub_nation = scrape_data.get_all_data()

    m = Movie(str(upc), pub_nation, movie_name, movie_year)
    movie = m.get_all_data()

    db = MovieDatabase()
    db.add_movie(movie)

    if movie_name is not []:
        return jsonify({'message': 'Found movie', 'movie': movie}), 200

    return jsonify({'message': 'Could not find any movies', 'upc': str(upc)}), 404


if __name__ == "__main__":
    app.run()
