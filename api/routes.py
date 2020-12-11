from api import controllers


def setup_routes(app):
    app.router.add_get('/', controllers.index, name='index')
    app.router.add_post(
        '/v1/create_car', controllers.create_car, name='create_car'
    )
