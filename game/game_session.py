from random import randint


class GameSession:
    def __init__(self, words: list, players, player_scores: dict):
        self.words = words
        self.players = players
        self.player_scores = player_scores
        self.current_word = ""
    def get_game_data(self):
        return self.words, self.players


    def start_round(self):
        pass
    #def update_game_data

    def get_random_word(self):
        rand_index = randint(0, len(self.words) - 1)
        if len(self.words) == 1:
            self.current_word = self.words[0]
        else:
            if self.words[rand_index] == self.current_word:
                self.words.pop(rand_index)
                rand_index += 1
                self.current_word = self.words[rand_index]
                print("SESSION: get_random_word: ", self.current_word)
                return
            else:
                self.current_word = self.words[rand_index]
                print("SESSION: get_random_word: ", self.current_word)
                self.words.pop(rand_index)
                return


    async def start_timer(self):
        pass