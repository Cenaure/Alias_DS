from aiogram import Router, types, F
router = Router()

@router.callback_query(F.data == "create_lobby")
async def createLobby(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text="да да мгм", 
        reply_markup=types.InlineKeyboardMarkup(
        inline_keyboard=[[
            types.InlineKeyboardButton(text="Почати гру", callback_data="start_game"),
            types.InlineKeyboardButton(text="Налаштування", callback_data="settings")
        ]]
    ))
