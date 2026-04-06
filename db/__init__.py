import os

from motor.motor_asyncio import AsyncIOMotorClient

from debug.DebugLogger import DebugLogger

_db = None
_client = None
async def connect_Db():
    global _db
    global _client
    _client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    DebugLogger.Console("Connected to mongo")
    _db = _client.get_database('alias')

def get_Db():
    if _db is None:
        raise RuntimeError("Db not inited!")
    else:
        return _db

