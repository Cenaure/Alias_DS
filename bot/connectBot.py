import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv
from bot.keyboards.main_menu import main_menu_kb
from aiogram import F
from bot.handlers import register_routes

dp = Dispatcher()
async def connectTGBot():
    load_dotenv()
    bot = Bot(token=os.getenv('BOT'))
    register_routes(dp)
    print("Started bot")
    await dp.start_polling(bot)
