import threading

from dol.dictionaryObj import DictionaryObj
from dol.gameObj import GameObj as Game
from dol.mapObj import MapObj as Map

class GameService:
    def __init__(self):
        self.__dictionary_game = DictionaryObj()
        self.__map = Map()

    def __game_is_available(self):
        for id_game, game in self.__dictionary_game.get_all().items():
            if len(game.players) < 2:
                return game
        return None

    def __new_game(self):
        _game = Game()
        self.__dictionary_game.insert(_game.id, _game)
        return _game

    def get_size_game(self, id_game):
        game: Game = self.__dictionary_game.get_by_id(id_game)
        return len(game.players)

    def add_player_in_game(self, id_player):
        _game = self.__game_is_available()
        if _game is None:
            _game = self.__new_game()
        _game.players.append(id_player)
        return _game.id

    def get_player_in_game(self, id_game):
        game: Game = self.__dictionary_game.get_by_id(id_game)
        return game.players

    def get_id_game_with_player(self, id_player):
        for id_game, game in self.__dictionary_game.get_all().items():
            if id_player in game.players:
                return game.id

    def set_thread_game_event(self, id_game, thread):
        game: Game = self.__dictionary_game.get_by_id(id_game)
        game.thread_game_event = thread

    def get_thread_game_event(self, id_game):
        game: Game = self.__dictionary_game.get_by_id(id_game)
        return game.thread_game_event

    def get_map(self):
        return self.__map

    def get_game(self, id):
        return self.__dictionary_game.get_by_id(id)

