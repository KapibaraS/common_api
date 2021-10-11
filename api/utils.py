import json
import logging
from asyncio import AbstractEventLoop
from functools import wraps
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


def call_once(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        if not inner.call:
            await func(*args, **kwargs)
            inner.call = True
    inner.call = False
    return inner


@call_once
async def create_index(db):
    await db.cars.create_index(
        [("vin_code", pymongo.TEXT)], unique=True, sparse=True
    )
