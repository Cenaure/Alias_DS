from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from bot.connectBot import dp
from bot.keyboards.main_menu import main_menu_kb

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Здарова гой! Я выдам тебе всё что хочешь, но нужно нажать кнопку", reply_markup=main_menu_kb())


@dp.callback_query('test')
async def testQuery(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('ДОБРО ПОШЛО')

