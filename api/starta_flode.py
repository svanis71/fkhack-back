from flask import request
from flask_restful import Resource


class StartaFlode(Resource):
    def get(self):
        pnr = request.headers['token']
        # Find pnr in db
        # if not found
        flode = 'A' if ord(pnr[-1]) % 2 == 0 else 'B', 204
        # else
        # flode = db.flode
        # Save starting time or create a new record in db

        return flode, 200
