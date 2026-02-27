from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_kb() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Створити лобі', callback_data="create_lobby"),
            InlineKeyboardButton(text='Список лобі', callback_data="list_lobby")
        ],
        [
            InlineKeyboardButton(text='Налаштування', callback_data="settings"),
            InlineKeyboardButton(text='Правила', callback_data="rules")
        ]
    ])
    return keyboard