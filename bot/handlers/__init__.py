from aiogram import Dispatcher
from bot.handlers.start import router as start_router
from bot.handlers.lobby import router as lobby_router

#тут розташована реєстрація для кожної, можна сказати, сторінки
def register_routes(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(lobby_router)