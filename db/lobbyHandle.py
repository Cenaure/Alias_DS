from db import get_Db
from motor.motor_asyncio import AsyncIOMotorClient
from aiogram import types

async def createLobbyDB(uid: int):
    db = get_Db()
    col = db.get_collection('lobbys')
    add = await col.insert_one({
        "host": uid,
        "status": "waiting", #тут будут ин гэйм и прочие 
        "players": [], #заглушко, потом тут будет принимать соо от юзера
        "pack": "none"
    })
    print("Lobby DB id: ", add.inserted_id)
    print("Lobby created, host_id: ", uid)


async def fetchLobbiesList():
    db = get_Db()
    col = db.get_collection('lobbys')
    # lobbysCount = await col.count_documents({})
    lobbys_list = col.find({"status": "waiting"}).limit(10) # поиск по статусу ожидания, знач игра не идёт.
    for lobby in lobbys_list: 
        print(lobby["host"]) #Not iterable пофиксить надо блин нафиг