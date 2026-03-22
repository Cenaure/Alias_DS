class GameSession:
    def __init__(self, words: list, players):
        self.words = words
        self.players = players

    #тут всю логику обмена данными в идеале, и таймер раундов и вызов пуш в БД. 
    def get_game_data(self):
        return self.words, self.players
