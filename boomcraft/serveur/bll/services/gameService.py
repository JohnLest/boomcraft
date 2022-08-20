import threading

from tool import *
from apis.boomcraftApi import BoomcraftApi
from apis.otherApi import *
from dol.dictionaryObj import DictionaryObj
from dol.gameObj import GameObj as Game
from dol.mapObj import MapObj as Map

class GameService:
    def __init__(self, boomcrat_api):
        self.__dictionary_game = DictionaryObj()
        self.__boomcraft_api: BoomcraftApi =boomcrat_api
        self.__map = Map()

    def __game_is_available(self):
        for id_game, game in self.__dictionary_game.get_all().items():
            if len(game.players) < 2:
                return game
        return None

    def __new_game(self):
        _game = Game()
        self.__dictionary_game.insert(_game.id, _game)
        self.__set_rarity(_game.id)
        return _game

    def __set_rarity(self, id_game):
        weight_resource = self.__boomcraft_api.get_weight_resource()
        _game: Game = self.__dictionary_game.get_by_id(id_game)
        for _weight_res in weight_resource:
            if _weight_res.get("name") == "gold":
                _game.rarity_gold = (1 / _weight_res.get("weight", 1000)) * 1000
        uri = "http://dataservice.accuweather.com/currentconditions/v1/"
        request = "27581?apikey=NM6IwoED21vbDTI6Fc7gosRt9A5rqNTu"
        weather = first_or_default(get_request(uri, request))
        temp = weather.get("Temperature").get("Metric").get("Value")
        if 17 < temp < 25:
            _game.rarity_food = 0
        elif 7 < temp <= 17:
            _game.rarity_food = (int(17 - temp / 2) * 0.1)
        elif 25 <= temp < 35:
            _game.rarity_food = (int(35 - temp / 2) * 0.1)
        else:
            _game.rarity_food = 0.7

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

