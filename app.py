from flask import Flask, json
from flask_cors import CORS, cross_origin

companies = [{"id": 1, "health": "20%"},
             {"id": 2, "health": "70%"}]

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/health', methods=['GET'])
@cross_origin()
def get_companies():
    return json.dumps(companies)


if __name__ == '__main__':
    app.run()
