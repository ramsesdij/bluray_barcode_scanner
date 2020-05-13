from flask import Flask, jsonify, request, make_response
from data import Data
import os
import requests

app = Flask(__name__)


@app.route('/analyse_barcode')
def analyse_barcode():
    upc = request.args.get('upc')
    data = Data(upc)
    movie_name, nation = data.search_upc()

    if movie_name is not []:
        return jsonify({'message': 'Found movie', 'movie_name': movie_name, 
            'pub_nation': nation, 'upc': str(upc)}), 200

    return jsonify({'message': 'Could not find any movies', 'upc': str(upc)}), 404


if __name__ == "__main__":
    app.run()
