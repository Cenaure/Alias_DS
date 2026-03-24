import discord
from bot.views.base import BaseView
from game.game_states import get_active_session
class RoundView(BaseView):
    menu_text = "Change to build text method later"
    def __init__(self, uid: int):
        self.session = get_active_session(uid)
        self.words, self.players = self.session.get_game_data()
        super().__init__(back_view=None)

    def wha(self):
        print("Inside round menu game data: ", self.words, self.players)
    @discord.ui.button(label="нэ", style=discord.ButtonStyle.primary, row=0)
    async def test_func(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.session.get_random_word()
        #заглушка