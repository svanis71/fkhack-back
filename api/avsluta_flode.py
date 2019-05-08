from flask import request
from flask_restful import Resource


class AvslutaFlode(Resource):
    def get(self):
        pnr = request.headers['token']
        # Find pnr in mongodb
        # Save a finish record
        return pnr, 200
