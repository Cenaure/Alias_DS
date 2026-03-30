from game.game_session import GameSession

active_sessions: dict[int, "GameSession"] = {}

def register_active_session(lobby_id: int, session: "GameSession"):
    if lobby_id not in active_sessions:
        active_sessions[lobby_id] = session
    print(f"Registered session {lobby_id}.")

def remove_active_session(lobby_id: int):
    if lobby_id in active_sessions:
        active_sessions.pop(lobby_id)
    print(f"Removed session {lobby_id}.")

def get_active_session(lobby_id: int):
    if lobby_id in active_sessions:
        print(f"Sent session {lobby_id}.")
        return active_sessions[lobby_id]
    else:
        return None

