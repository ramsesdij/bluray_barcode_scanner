from flask import Flask, jsonify, request
from src.scrape_data import ScrapeData
from src.api_data import APIData

app = Flask(__name__)


@app.route('/analyse_barcode')
def analyse_barcode():
    upc = request.args.get('upc')
    scrape_data = ScrapeData(upc)
    movie_name, movie_year, pub_nation = scrape_data.get_all_data()

    meta_data = APIData(movie_name, movie_year)
    meta_data.get_all_data()

    if movie_name is not []:
        return jsonify({'message': 'Found movie', 'movie_name': movie_name, 'movie_year': movie_year,
            'pub_nation': pub_nation, 'upc': str(upc)}), 200

    return jsonify({'message': 'Could not find any movies', 'upc': str(upc)}), 404


if __name__ == "__main__":
    app.run()
