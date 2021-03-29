from flask import Flask, json, request
from flask_cors import CORS, cross_origin
from functions.API.get_statuses import *
from functions.API.post_apples import *
from functions.initializations import *
import json
import os


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
detector = init()


@app.route('/status', methods=['GET'])
@cross_origin()
def get_statuses():
    return json.dumps(get_statuses_all())


@app.route('/status', methods=['POST'])
@cross_origin()
def post_apples():
    img_string = request.json['image']
    string_data = process_apples(detector, str(img_string))
    json_data = json.dumps(string_data)

    # docker change
    # with open('resources\\temp_db\\data.json', 'w', encoding='utf-8') as f:
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(string_data, f, ensure_ascii=False, indent=4)

    return json_data


if __name__ == '__main__':
    app.run()
