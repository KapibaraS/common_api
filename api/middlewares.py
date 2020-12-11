import logging
import traceback
from typing import Any

from aiohttp import web
from aiohttp.web_exceptions import HTTPMethodNotAllowed, HTTPNotFound
from pymongo.errors import DuplicateKeyError

from api.errors import ValidationError, BaseApiError, MethodNotAllowedError, \
    RouteNotFoundError

from api.utils import error_response

log = logging.getLogger(__name__)


async def db_handler(app, handler):
    @web.middleware
    async def middleware(request):
        request.db = app['mongodb_connection']
        request.db_cli = app['mongodb_client']
        response = await handler(request)
        return response
    return middleware


@web.middleware
async def all_error_response_wrapper(
        request: web.Request, handler: Any
) -> Any:
    try:
        response = await handler(request)
        return response
    except ValidationError as e:
        return error_response(
            message=e.text,
            error_code=e.code,
            status=e.status,
            errors=e.errors,
        )
    except BaseApiError as e:
        tb = traceback.format_exc()
        log.error(
            '[error_response_wrapper][api_error]',
            extra={
                'request_path': request.raw_path,
                'response_message': e.text,
                'response_code': e.code,
                'response_status': e.status,
                'traceback': tb,
            }
        )
        return error_response(
            message=e.text,
            error_code=e.code,
            status=e.status,
            data=e.data,
        )
    except DuplicateKeyError as e:
        return error_response(
            message=e.text,
            error_code=e.code,
            status=e.status,
        )
    except HTTPMethodNotAllowed as e:
        return error_response(
            message=MethodNotAllowedError.text,
            error_code=MethodNotAllowedError.code,
            status=MethodNotAllowedError.status,
        )
    except HTTPNotFound as e:
        return error_response(
            message=RouteNotFoundError.text,
            error_code=RouteNotFoundError.code,
            status=RouteNotFoundError.status,
        )
    except Exception as e:
        log.exception(
            '[error_response_wrapper][unhandled_exception]', exc_info=e
        )
        return error_response(
            message=UnhandledServerError.text,
            error_code=UnhandledServerError.code,
            status=UnhandledServerError.status,
        )
