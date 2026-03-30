import discord
from bot.views.base import BaseView
from game.game_states import get_active_session


class RoundView(BaseView):
    def __init__(self, uid: int, interaction: discord.Interaction):
        self.session = get_active_session(uid)
        self.players, self.current_word = self.session.get_game_data()
        self.menu_text = self._build_text(words=[self.current_word])
        self.words = [self.current_word]
        self.interaction = interaction
        super().__init__(back_view=None)

    @staticmethod
    def _build_text(words):
        words_str = "\n".join(f"{w}" for w in words[:-1])
        return f"{words_str} <-"

    async def update_text(self):
        word = self.session.get_random_word(self.current_word)
        self.words.append(word)
        text = self._build_text(words=self.words)
        await self.interaction.edit_original_response(content=text, view=self)

    @discord.ui.button(label="✅ Вгадав", style=discord.ButtonStyle.success, row=0)
    async def like_button(self, button: discord.ui.Button, interaction: discord.Interaction):

        await self.update_text()

    @discord.ui.button(label="❎ Не вгадав", style=discord.ButtonStyle.danger, row=0)
    async def dislike_button(self, button: discord.ui.Button, interaction: discord.Interaction):

        await self.update_text()