from random import randint

from debug.DebugLogger import DebugLogger


class GameSession:
    def __init__(self, words: list, players, player_scores: dict, teams: dict):
        self.words = words
        self.players = players
        self.teams = teams
        self.player_scores = player_scores
        self.current_word = self.get_random_word("")
    def get_game_data(self):
        return self.players, self.current_word

    def start_round(self):
        pass

    def update_player_scores(self, uid: int, status: bool):
        if self.player_scores[uid] == 0:
            return
        if status:
            self.player_scores[uid] += 1
        else:
            self.player_scores[uid] -= 1

    def get_random_word(self, word):
        rand_index = randint(0, len(self.words) - 1)
        if len(self.words) == 1:
            word = self.words[0]
            return word
        else:
            if self.words[rand_index] == word:
                self.words.pop(rand_index)
                rand_index += 1
                word = self.words[rand_index]
                DebugLogger.Console("SESSION: get_random_word: ", word)
                return word
            else:
                word = self.words[rand_index]
                DebugLogger.Console("SESSION: get_random_word: ", word)
                self.words.pop(rand_index)
                return word


    async def start_timer(self):
        pass