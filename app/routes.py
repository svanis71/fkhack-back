from api import StartaFlode, AvslutaFlode


def create_routes(api):
    api.add_resource(StartaFlode, '/starta')
    api.add_resource(AvslutaFlode, '/avsluta')