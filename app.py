from flask import Flask, json
from flask_cors import CORS, cross_origin

companies = [{"id": 1, "name": "Company One"},
             {"id": 2, "name": "Company Two"}]

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/companies', methods=['GET'])
@cross_origin()
def get_companies():
    return json.dumps(companies)


if __name__ == '__main__':
    app.run()
