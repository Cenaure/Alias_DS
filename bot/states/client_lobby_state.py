from bot.views.lobby.lobby_player_menu import LobbyClientView
from debug.DebugLogger import DebugLogger

active_client_lobbys: dict[int, "LobbyClientView"] = {}

def register_client_lobby(uid: int ,view: "LobbyClientView"):
    if uid not in active_client_lobbys:
        active_client_lobbys[uid] = view
    DebugLogger.Console("CLIENT LOBBY: Registered", active_client_lobbys)

def unregister_client_lobby(uid: int):
    if uid in active_client_lobbys:
        DebugLogger.Console("LOBBY STATE: Poped lobby with UID, ", uid)
        active_client_lobbys.pop(uid)

def get_client_lobby(uid: int):
    DebugLogger.Console(f"Trying to get client lobby with id: {uid}")
    lobby = active_client_lobbys.get(uid)
    if lobby is not {}:
        DebugLogger.Console("LOBBY STATE: Found lobby with id", uid)
        type(lobby)
        return lobby
    else:
        DebugLogger.Console("LOBBY STATE: No lobby with id", uid)
        return None