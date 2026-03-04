from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import db.lobbyHandle as dbLobby
from bot.keyboards.lobbies_list_board import lobbies_list_kb
from bot.handlers.start import main_menu
from bot.menus.LobbyMenu import lobby_menu, lobby_menu_message
import asyncio

from bot.states.states import JoinLobby
from db.lobbyHandle import passLobby
from db.userHandle import removePlayerfromDB

router = Router()

@router.callback_query(F.data == "create_lobby")
async def createLobby(callback: types.CallbackQuery):
    await dbLobby.createLobbyDB(callback.from_user.id, callback.from_user.full_name)
    await lobby_menu(callback.from_user.id, callback)


@router.callback_query(F.data == "list_lobby")
async def lobbiesList(callback: types.CallbackQuery):
    lobbies = await dbLobby.fetchLobbiesList()
    keyboard = await lobbies_list_kb(lobbies)
    await callback.message.edit_text(
        text="Список лобі",
        reply_markup=keyboard.as_markup()
        #types.InlineKeyboardMarkup(
        #inline_keyboard=)
    )

@router.callback_query(F.data == "quit_lobby")
async def quitLobby(callback: types.CallbackQuery):
    uid = callback.from_user.id
    name = callback.from_user.full_name
    await asyncio.gather(dbLobby.deleteLobbyDB(uid, name),main_menu(None, callback))
    await removePlayerfromDB(uid)

@router.callback_query(F.data.startswith("join_lobby:"))#LobbyCallback.filter(F.data == "join"))
async def joinLobby(callback: types.CallbackQuery, state: FSMContext):
    print("Joining lobby...")
    await asyncio.gather(
        state.set_state(JoinLobby.wait_code),
        callback.bot.send_message(callback.from_user.id, "Введіть код лобі")
    )
#Убрать публичный список, вместо этого чисто по коду присоединение

@router.message(JoinLobby.wait_code)
async def connectLobby(message: types.Message, state: FSMContext):
    if not message.text.isnumeric():
        await message.answer("Лобі не знайдено. Можливо код не вірний!",
                             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                [
                                    InlineKeyboardButton(text='Назад', callback_data="start"),
                                ]])
                             )
        return


    lobby_code=message.text.strip()
    lobby = await passLobby(int(lobby_code))


    if not lobby:
        await message.answer("Лобі не знайдено. Можливо код не вірний!",
                             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                [
                                    InlineKeyboardButton(text='Назад', callback_data="start"),
                                ]])
                             )
        return
    if lobby['status'] != "waiting":
        await message.answer("Гра вже почалась")
        await state.clear()
        return


    lobby_id = lobby['host']
    user_id = message.from_user.id
    print("Lobby_ID In joinLobby, ", lobby_id)
    await dbLobby.joinLobbyDB(lobby_id , user_id, message.from_user.full_name)
    await message.bot.send_message(lobby_id, f"Гравець {message.from_user.full_name} приєднався до лобі")
    await lobby_menu_message(lobby_id, message)
