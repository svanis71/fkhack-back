from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api

from .routes import create_routes

application = Flask(__name__)
cors = CORS(application)
api = Api(application)

create_routes(api)
