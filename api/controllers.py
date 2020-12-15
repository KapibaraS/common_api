from aiohttp import web

from api.documents_mongo import Car
from api.utils import (
    extract_data_from_json, serialize_car, is_valid_data,
)


async def index(request):
    cursor = request.db.cars.find({})
    cars = await cursor.to_list(length=25)
    return web.json_response(cars and [serialize_car(car) for car in cars])


async def create_car(request):
    post_data = await extract_data_from_json(request)
    is_valid_data(post_data)
    car = Car(request.db, **post_data)
    await car.create()
    return web.Response(text="create", status=201)


async def get_car(request):
    car = await Car(request.db).get(request.match_info['car_id'])
    return web.json_response(serialize_car(car) if car else {})


async def delete_car(request):
    car = await Car(request.db).delete(request.match_info['car_id'])
    return web.json_response({"status": 100})
