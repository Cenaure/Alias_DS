from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message

from db.lobbyHandle import getLobbyCode


async def lobby_menu(hostid: int, callback: CallbackQuery):
    if callback.from_user.id == hostid:
        code = await getLobbyCode(hostid)
        return await callback.message.edit_text(
            text=f"Ви хост \n Ваш код лобі {code}",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[
                    InlineKeyboardButton(text="Почати гру", callback_data="start_game"),
                    InlineKeyboardButton(text="Налаштування", callback_data="settings")
                ],
                    [
                        InlineKeyboardButton(text="Обрати пак", callback_data="pack"),
                        InlineKeyboardButton(text="Вийти", callback_data="quit_lobby")
                    ]
                ]
            ))
    else:
        return await callback.message.edit_text(
            text="Очікуйте початку гри",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[
                    InlineKeyboardButton(text="Вийти", callback_data="quit_lobby")
                ]]
            ))


async def lobby_menu_message(hostid: int, message: Message):
    if message.from_user.id == hostid:
        code = await getLobbyCode(hostid)
        return await message.answer(
            text=f"Ви хост \n Ваш код лобі {code}",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[
                    InlineKeyboardButton(text="Почати гру", callback_data="start_game"),
                    InlineKeyboardButton(text="Налаштування", callback_data="settings")
                ],
                    [
                        InlineKeyboardButton(text="Обрати пак", callback_data="pack"),
                        InlineKeyboardButton(text="Вийти", callback_data="quit_lobby")
                    ]
                ]
            ))
    else:
        return await message.answer(
            text="Очікуйте початку гри",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[
                    InlineKeyboardButton(text="Вийти", callback_data="quit_lobby")
                ]]
            ))