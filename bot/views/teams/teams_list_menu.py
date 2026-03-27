
import discord

from bot.views.base import BaseView
from game.game_teams import register_team, get_lobby_teams, join_team


class TeamsListView(BaseView):
    def __init__(self, interaction: discord.Interaction, host_id: int) -> None:
        self.host_id = host_id
        self.menu_text = "Оберіть команду, або створіть нову"
        self.interaction = interaction
        self.teams = get_lobby_teams(self.host_id)
        super().__init__(back_view=None)
        for team in self.teams:
            print("DEBUG: teams:", team)
            self.add_item(TeamButton(team=team, row=len(self.teams) // 3, lobby_id=self.host_id))
        self.add_item(CreateTeam(row=4, uid=self.host_id, teamlistview=self))

    # async def update_teams(self):
    #     self.teams = get_lobby_teams(self.host_id)
    #     print("SELF TEAMS: ", self.teams)
    #     for team in self.teams:
    #         print("DEBUG: teams:", team)
    #         self.add_item(TeamButton(team=team, row=len(self.teams) // 3, lobby_id=self.host_id))
    #     await self.interaction.edit_original_response(content=self.menu_text, view=self)
class TeamButton(discord.ui.Button):
    def __init__(self, team, row: int, lobby_id: int):
        self.team = team
        self.lobby_id = lobby_id
        super().__init__(
            label=f"Команда '{team}'",
            style=discord.ButtonStyle.primary,
            custom_id=f"team_{team}",
            row=row
        )

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.name != self.team:
            join_team(lobby_id=self.lobby_id, player_id=interaction.user.id, team_name=self.team['name'])
        else:
            print(f"TEAMS: Exception! Cannot join player {interaction.user.name} to self team")



class CreateTeam(discord.ui.Button):
    def __init__(self, row: int, uid: int, teamlistview: TeamsListView):
        self.uid = uid
        self.teamlistview = teamlistview
        super().__init__(
            label="Створити [+]",
            style=discord.ButtonStyle.success,
            row=row,
            )
    async def callback(self, interaction: discord.Interaction):
        from bot.states.lobby_state import get_views
        register_team(self.uid, interaction.user.name,[interaction.user.id])
        view = get_views(self.uid)
        await view.refresh_lobby(team_name=interaction.user.name)
        #await self.teamlistview.update_teams()
        await interaction.response.edit_message(
            content=view.menu_text,
            view=view
        )
