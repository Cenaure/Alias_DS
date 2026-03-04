from aiogram.fsm.state import State, StatesGroup

class JoinLobby(StatesGroup):
    wait_code = State()