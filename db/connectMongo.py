import asyncio
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

db = None
collection = None

async def connect_Db():
    global db
    global collection
    
    client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    print("Connected to mongo")
    db = client.get_database('alias')
    collection = db.get_collection('packs')

async def get_Db():
    return db

async def get_Collection():
    return collection
