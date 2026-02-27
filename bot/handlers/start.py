from aiogram import Router, types
from aiogram.filters import Command
from bot.keyboards.main_menu import main_menu_kb
router = Router()

@router.message(Command("start"))
async def start_Handler(message: types.Message) -> any:
    await message.answer(
        text="Привіт софійко це зайчик джуді гопс!",
        reply_markup=main_menu_kb()
        )
    

@router.message(Command("test"))
async def message_Handler(message: types.Message) -> any:
    await message.answer("Hello from routah!")