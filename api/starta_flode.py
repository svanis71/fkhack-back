import os
from datetime import datetime

from flask import request
from flask_restful import Resource
from pymongo import MongoClient
import os
import secrets

MONGODB_CONNECTION = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')


class StartaFlode(Resource):
    def get(self):
        pnr = request.headers['token']
        # Find pnr in db
        mongo_client = MongoClient(MONGODB_CONNECTION)
        # if not found
        db = mongo_client['heroku_ssj5qmzb']
        subjects = db.subjects

        flode = 'A' if ord(pnr[-1]) % 2 == 0 else 'B'

        # else
        # flode = db.flode
        # Save starting time or create a new record in db
        start_ts = datetime.now().timestamp()
        subject = {'pnr': pnr, 'flode': flode, 'start_at': start_ts, 'ref': secrets.token_hex(16), 'end_at': None}
        subjects.insert_one(subject)
        print(subject)
        return {'ref': subject['ref'], 'flode': flode}, 200
