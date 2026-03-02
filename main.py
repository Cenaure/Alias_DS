import asyncio
import db
from bot.connectBot import connectTGBot
from db.lobbyHandle import flushDb
from db.userHandle import flushPlayersDB


async def main():
    await asyncio.gather(db.connect_Db(), connectTGBot(), flushDb(), flushPlayersDB())
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped")
    

