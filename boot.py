from flask import Flask, jsonify, request, make_response
from data import Data
import os
import requests

app = Flask(__name__)

@app.route('/analyse_barcode')
def analyse_barcode():
    upc = request.args.get('upc')
    print(upc)
    data = Data(upc)
    data.search_upc()
    return str(upc)


if __name__ == "__main__":
    app.run()
