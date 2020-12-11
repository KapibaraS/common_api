from typing import Dict


class BaseApiError(Exception):
    text = ''
    data = None
    errors = None
    status = 400
    code = 1

    def __init__(
        self, message: str = None, status: int = None, code: int = None,
        data: Dict = None, errors: Dict = None
    ) -> None:
        super().__init__(message)
        self.text = message or self.text
        self.status = status or self.status
        self.code = code or self.code
        self.data = data or self.data
        self.errors = errors or self.errors


class BadJSONRequestDataError(BaseApiError):
    text = 'bad json in request'
    code = 1001


class ValidationError(BaseApiError):
    text = 'invalid data in request'
    code = 1002


class MethodNotAllowedError(BaseApiError):
    status = 405
    text = 'method is not allowed for this route'
    code = 1003


class RouteNotFoundError(BaseApiError):
    status = 404
    text = 'route not found'
    code = 1004


class UnhandledServerError(BaseApiError):
    status = 500
    text = 'server error'
    code = 1000
