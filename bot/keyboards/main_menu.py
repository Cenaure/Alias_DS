from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_kb() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Створити лобі', callback_data="create_lobby"),
            InlineKeyboardButton(text='Список лобі', callback_data="list_lobby")
        ],
        [
            InlineKeyboardButton(text='Статистика', callback_data="leaderboard") #это я реализую годам к 25
        ]
    ])
    return keyboard