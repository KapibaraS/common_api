import aiohttp_cors

from api import controllers


def setup_routes(app):
    app.router.add_get('/', controllers.index, name='index')
    app.router.add_post(
        '/v1/create_car', controllers.create_car, name='create_car'
    )
    app.router.add_get(
        '/v1/get_car/{car_id}', controllers.get_car, name='get_car'
    )
    app.router.add_delete(
        '/v1/delete_car/{car_id}', controllers.delete_car, name='delete_car'
    )
    app.router.add_get(
        '/v1/get_cars/{page}', controllers.get_cars, name='get_cars'
    )
    # app.router.add_route('*', '/{tail:.*}', controllers.index)

    # app.router.add_static('/static', './api/build')
    cors = aiohttp_cors.setup(app, defaults={"*": aiohttp_cors.ResourceOptions(
                                    allow_credentials=True,
                                    expose_headers="*",
                                    allow_headers="*",
                                    )})

    for route in list(app.router.routes()):
        cors.add(route)
