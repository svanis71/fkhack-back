from datetime import datetime

from flask import request
from flask_restful import Resource
from pymongo import MongoClient

from api.starta_flode import MONGODB_CONNECTION


class AvslutaFlode(Resource):
    def get(self):
        ref = request.headers['token']

        mongo_client = MongoClient(MONGODB_CONNECTION)
        # if not found
        db = mongo_client['heroku_ssj5qmzb']
        subjects = db.subjects
        query = {"ref": ref}
        update_end_time = {"$set": {"end_at": datetime.now().timestamp()}}
        db.subjects.update_one(query, update_end_time)
        cur = subjects.find_one({"ref": ref})
        print(cur)
        # Find pnr in mongodb
        # Save a finish record
        return ref, 200
