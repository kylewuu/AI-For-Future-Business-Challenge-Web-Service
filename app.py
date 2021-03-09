from functions.image_detection import image_detection
from flask import Flask, json
from flask_cors import CORS, cross_origin
from functions.image_detection import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/health', methods=['GET'])
@cross_origin()
def get_companies():
    return json.dumps(image_detection())


if __name__ == '__main__':
    app.run()
