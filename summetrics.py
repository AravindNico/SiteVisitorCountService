from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
CORS(app)

from api.v1.api import api
app.register_blueprint(api)

with open('config.json', 'r') as f:
    config = json.load(f)

enabledEnv = config['EnabledEnv']
appIp = config[enabledEnv]['AppIp']
appPort = config[enabledEnv]['AppPort']


@app.route('/', methods=['post', 'get'])
def home():
    return jsonify({"content": "API SERVERS"})


if __name__ == '__main__':
    app.run(host=appIp, port=appPort, debug=True)
