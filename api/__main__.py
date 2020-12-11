import asyncio

from aiohttp import web

from api.app import create_app
from api.config import config

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass


if __name__ == '__main__':
    if config['debug']:
        import aioreloader
        aioreloader.start()
    app = create_app(config)
    web.run_app(app)
