from api import StartaFlode, AvslutaFlode, Ping, Statistik


def create_routes(api):
    api.add_resource(Ping, '/')
    api.add_resource(StartaFlode, '/starta')
    api.add_resource(AvslutaFlode, '/avsluta')
    api.add_resource(Statistik, '/statistik')