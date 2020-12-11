import json
import logging
from asyncio import AbstractEventLoop
from typing import Dict, Any

import pymongo
from aiohttp import web
from aiohttp.web_response import json_response
from motor.motor_asyncio import AsyncIOMotorClient

from api.errors import BadJSONRequestDataError, ValidationError
from api.schemas import json_create_car_schema

log = logging.getLogger(__name__)

VIN_CODE_WIKI_URL = (
    'https://en.wikipedia.org/wiki/Vehicle_identification_number'
)


def mongo_conn_startup(dsn: str, db_name: str, loop: AbstractEventLoop):
    client = AsyncIOMotorClient(
        dsn, io_loop=loop,
    )
    db_connection = client[db_name]
    return client, db_connection


def mongo_conn_shutdown(mongo_client: AsyncIOMotorClient) -> None:
    mongo_client.close()


async def extract_data_from_json(request: web.Request) -> Dict[str, Any]:
    try:
        return await request.json()
    except json.decoder.JSONDecodeError:
        log.error('[Error] Bad json request')
        raise BadJSONRequestDataError


def serialize_car(car):
    return {
        "car_id": str(car['_id']),
        "manufacturer": car['manufacturer'],
        "model": car['model'],
        "year_production": car['year_production'],
        "color": car['color'],
        "vin_code": car['vin_code'],
    }


def error_response(
        message: str, error_code: int = 1000,
        errors: str = None,
        status: int = 400,
        data: Dict = None
) -> web.Response:
    return json_response(
        {
            'data': data or {},
            'error_code': error_code,
            'message': message,
            'errors': errors or {},
        },
        status=status
    )


def is_valid_data(data):
    json_create_car_schema.check(data)
    errors = {}
    if len(data['model']) > 200:
        errors['model'] = 'model must be less than 200 characters'

    if len(data['manufacturer']) > 200:
        errors['manufacturer'] = 'manufacturer must be less than 200 characters'  # noqa

    if not data['year_production'].isdigit():
        errors['year_production'] = 'year_production must be 4 digits'
    elif len(data['year_production']) != 4:
        errors['year_production'] = 'year_production must be 4 digits'
    if len(data['color']) > 100:
        errors['color'] = 'invalid color'

    if len(data['vin_code']) > 17:
        errors['vin_code'] = (
            f'vin_code must be 17 characters, '
            f'show link {VIN_CODE_WIKI_URL}'
        )

    if errors:
        raise ValidationError(errors=errors)


def call_once(func):
    async def inner(*args, **kwargs):
        if not inner.call:
            await func(*args, **kwargs)
            inner.call = True
    inner.call = False
    return inner


@call_once
async def create_index(db):
    await db.cars.create_index([("vin_code", pymongo.TEXT)], unique=True)
