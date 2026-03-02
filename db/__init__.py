import os
from motor.motor_asyncio import AsyncIOMotorClient

_db = None
_client = None
async def connect_Db():
    global _db
    global _client
    _client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    print("Connected to mongo")
    _db = _client.get_database('alias')

def get_Db():
    if _db is None:
        raise RuntimeError("Db not inited!")
    else:
        return _db

