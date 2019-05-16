from flask_restful import Resource
from pymongo import MongoClient

from api.starta_flode import MONGODB_CONNECTION
from statistics import median

class Statistik(Resource):
    def getFlodeStatistics(self, subjects, flode=None):
        allData = [r for r in subjects.find(flode and {'flode': flode} or {})]
        tid = [int(x['end_at'] - x['start_at']) for x in allData if x['end_at'] is not None]
        retobj = {
            'started': len(allData),
            'ended': len([x for x in allData if x['end_at'] is not None]),
            'median': tid and median(tid) or 0
        }
        return retobj

    def getFlodeB(self):
        pass


    def get(self):
        mongo_client = MongoClient(MONGODB_CONNECTION)
        # if not found
        db = mongo_client['heroku_ssj5qmzb']
        subjects = db.subjects
        statistics = {
            'total': self.getFlodeStatistics(subjects),
            'A': self.getFlodeStatistics(subjects, 'A'),
            'B': self.getFlodeStatistics(subjects, 'B')
        }

        return statistics, 200