from aiohttp import web

from api.documents_mongo import Car
from api.schemas import CarSchema
from api.utils import extract_data_from_json, CONTENT

QUANTITY_CARS_ON_PAGE = 10


async def index(request):
    return web.Response(body=CONTENT, content_type='text/html')


async def get_cars(request):
    page = request.match_info['page']
    skip_count = int(page) * QUANTITY_CARS_ON_PAGE if int(page) > 1 else 0

    cursor = request.db.cars.find().skip(skip_count)
    cars = await cursor.to_list(length=QUANTITY_CARS_ON_PAGE)

    return web.json_response(
        cars and [CarSchema().dump(car) for car in cars]
    )


async def create_car(request):
    post_data = await extract_data_from_json(request)
    schema = CarSchema()
    schema.load(post_data)
    car = Car(request.db, **post_data)
    await car.create()
    return web.Response(text="create", status=201)


async def get_car(request):
    car = await Car(request.db).get(request.match_info['car_id'])
    return web.json_response(CarSchema().dump(car) if car else {})


async def delete_car(request):
    await Car(request.db).delete(request.match_info['car_id'])
    return web.json_response({"status": 200})
