from game.game_session import GameSession

active_sessions: dict[int, "GameSession"] = {}

def register_active_session(uid: int, session: "GameSession"):
    if uid not in active_sessions:
        active_sessions[uid] = session
    print(f"Registered session {uid}.")

def remove_active_session(uid: int):
    if uid in active_sessions:
        active_sessions.pop(uid)
    print(f"Removed session {uid}.")

def get_active_session(uid: int):
    if uid in active_sessions:
        print(f"Sent session {uid}.")
        return active_sessions[uid]
    else:
        return None

