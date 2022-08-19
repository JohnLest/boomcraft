import json
import copy

from models.playerInfoModel import PlayerInfoModel
from apis.boomcraftApi import BoomcraftApi
from dol.playerObj import PlayerObj as Player
from dol.dictionaryObj import DictionaryObj


class PlayerService:
    def __init__(self):
        self.__dictionary_player = DictionaryObj()
        self.boomcraft_api = BoomcraftApi()

    def __get_user(self, **data):
        user = None
        if data.get("connection_type") == "login":
            data.pop("connection_type")
            user = self.boomcraft_api.connect(data.get("mail"), data.get("password"))
        elif data.get("connection_type") == "new":
            data.pop("connection_type")
            user = self.boomcraft_api.post_new_user(json.dumps(data))
        elif data.get("connection_type") == "facebook":
            data.pop("connection_type")
            user = self.boomcraft_api.connect_with_facebook(json.dumps(data))
        if user is None or user[0] >= 400:
            return "Error"
        return user[1]

    def __get_own_resources(self, id_player):
        resources = self.boomcraft_api.get_resources_by_id(id_player)
        return resources

    def __set_game_resources(self, own_resources):
        resources = copy.deepcopy(own_resources)
        for _resources in resources:
            _resources.update({"quantity": 0})
        return resources

    def new_player(self, key_socket, **data):
        """
        if ``connection_type`` = "login"\n
        use ``mail`` and ``password``\n
        elif ``connection_type`` = "new":\n
        use ``pseudo``, ``mail`` and ``password``\n
        elif ``connection_type`` = "facebook":\n
        use ``id``, ``name``, ``email``\n
        :return: user
        """
        _player = self.__get_user(**data)
        if _player == "Error" or _player is None:
            return None
        _own_resources = self.__get_own_resources(_player.get("id_user"))
        _game_resources = self.__set_game_resources(_own_resources.get("resource"))
        p_model = PlayerInfoModel(user=_player,
                                  own_resources=_own_resources.get("resource"),
                                  game_resources=_game_resources,
                                  key_socket=key_socket)
        player = Player(p_model)
        self.__dictionary_player.insert(p_model.user.id_user, player, )
        return p_model

    def get_socket(self, id_player):
        player: Player = self.__dictionary_player.get_by_id(id_player)
        return player.model_player.key_socket

    def update_resources(self, id_user, game_resources: dict):
        player: Player = self.__dictionary_player.get_by_id(id_user)
        p_model: PlayerInfoModel = player.model_player
        for _game_res in p_model.game_resources:
            _game_res.quantity = game_resources.get(_game_res.resource, 0)
        for _own_res in p_model.own_resources:
            _own_res.quantity = _own_res.quantity - game_resources.get(_own_res.resource, 0)
        return p_model

    def get_player_by_id(self, id_player):
        return self.__dictionary_player.get_by_id(id_player)

    def farm_resources(self, id_user, farm_resources: dict):
        player: Player = self.__dictionary_player.get_by_id(id_user)
        p_model: PlayerInfoModel = player.model_player
        for _game_res in p_model.game_resources:
            _game_res.quantity = _game_res.quantity + farm_resources.get(_game_res.resource, 0)
        return p_model

    def check_if_resource_available(self, id_player, cost: dict):
        player: Player = self.__dictionary_player.get_by_id(id_player)
        p_model: PlayerInfoModel = player.model_player
        for _game_res in p_model.game_resources:
            if _game_res.quantity < cost.get(_game_res.resource, 0):
                return None
        for _game_res in p_model.game_resources:
            _game_res.quantity = _game_res.quantity - cost.get(_game_res.resource, 0)
        return p_model
