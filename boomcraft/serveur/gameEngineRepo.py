import uuid


class GameEngineRepo:
    def __init__(self):
        self.game_lst: dict = {}

    def __game_is_available(self):
        for id_game, user_lst in self.game_lst.items():
            if len(user_lst) < 2:
                return id_game
        return None

    def __new_game(self):
        id_game = str(uuid.uuid4())
        self.game_lst.update({id_game: []})
        return id_game

    def add_player_in_game(self, player):
        id_game = self.__game_is_available()
        if id_game is None:
            id_game = self.__new_game()
        self.game_lst.get(id_game).append(player)
