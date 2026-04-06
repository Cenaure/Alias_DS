from bot.views.packs.packs_mypacks_menu import PacksListView
from debug.DebugLogger import DebugLogger

active_pack_views: dict[int, "PacksListView"] = {}

def register_pack_view(uid: int ,view: "PacksListView"):
    active_pack_views[uid] = view
    DebugLogger.Console("pack STATE: active_pack_views", active_pack_views)

def unregister_pack_view(uid: int):
    if uid in active_pack_views:
        active_pack_views.pop(uid)
        DebugLogger.Console("pack STATE: Poped active_pack ", active_pack_views)

def get_pack_view(uid: int):
    return active_pack_views.get(uid, {})