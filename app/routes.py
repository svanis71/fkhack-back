from api import StartaFlode, AvslutaFlode
from api.statistik import Statistik


def create_routes(api):
    api.add_resource(StartaFlode, '/starta')
    api.add_resource(AvslutaFlode, '/avsluta')
    api.add_resource(Statistik, '/statistik')