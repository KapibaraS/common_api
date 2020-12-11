from aiohttp import web

from api.utils import (
    extract_data_from_json, serialize_car, is_valid_data, create_index,
)


async def index(request):
    cursor = request.db.cars.find({})
    cars = await cursor.to_list(length=25)
    return web.json_response(cars and [serialize_car(car) for car in cars])


async def create_car(request):
    post_data = await extract_data_from_json(request)
    is_valid_data(post_data)
    collection = request.db.cars
    await collection.insert_one(post_data)
    return web.Response(text="create")



