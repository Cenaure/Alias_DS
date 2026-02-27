import os
import asyncio
from db import connect_Db
from db.packs import addPack
from bot.connectBot import connectTGBot


async def main():
    await connect_Db()
    await connectTGBot()
    # await addPack(input("Тестовое имя записи: "))
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped")
    

