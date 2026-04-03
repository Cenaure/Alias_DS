from bot.views.game.round_menu import RoundView

active_rounds: dict[int, "RoundView"] = {}

def register_round_view(lobby_id: int, round_view: RoundView):
    if lobby_id not in active_rounds:
        active_rounds[lobby_id] = round_view
        print(f"ROUND REGISTER: Registered round with lobby_id {lobby_id}")

def get_round_by_lobby_id(lobby_id: int):
    if lobby_id not in active_rounds:
        return None
    return active_rounds[lobby_id]