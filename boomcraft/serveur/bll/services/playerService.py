import json
import copy

from apis.boomcraftApi import BoomcraftApi
from apis.pongApi import PongApi
from apis.flappyApi import FlappyApi
from models.playerInfoModel import PlayerInfoModel
from dol.playerObj import PlayerObj as Player
from dol.dictionaryObj import DictionaryObj


class PlayerService:
    def __init__(self, boomcraft_api, pong_api, flappy_api):
        self.__dictionary_player = DictionaryObj()
        self.__pong_api: PongApi = pong_api
        self.__boomcraft_api: BoomcraftApi = boomcraft_api
        self.__flappy_api: FlappyApi = flappy_api

    def __get_user(self, **data):
        user = None
        if data.get("connection_type") == "login":
            data.pop("connection_type")
            user = self.__boomcraft_api.connect(data.get("mail"), data.get("password"))
        elif data.get("connection_type") == "new":
            data.pop("connection_type")
            user = self.__boomcraft_api.post_new_user(json.dumps(data))
        elif data.get("connection_type") == "facebook":
            data.pop("connection_type")
            user = self.__boomcraft_api.connect_with_facebook(json.dumps(data))
        elif data.get("connection_type") == "pong":
            data.pop("connection_type")
            user = self.__pong_api.login(json.dumps(data))
            user_data: dict = user[1]
            user_bc = None
            if not self.__check_if_user_exist(user_mail=user_data.get("email")):
                user_bc = self.__boomcraft_api.post_new_user(json.dumps({"pseudo": user_data.get("username"),
                                                                        "mail": user_data.get("email"),
                                                                        "password": user_data.get("id")}))
            else:
                user_bc = self.__boomcraft_api.connect(user_data.get("email"), user_data.get("id"))
            if user_bc is None or user_bc[0] >= 400:
                return "Error"
            user_bc_data: dict = user_bc[1]
            user_bc_data.update({"token": user_data.get("token")})
            return user_bc_data
        elif data.get("connection_type") == "flappy":
            data.pop("connection_type")
            user = self.__flappy_api.login(json.dumps(data))
            user_data: dict = user[1]
            user_bc = None
            if not self.__check_if_user_exist(user_mail=data.get("email")):
                user_bc = self.__boomcraft_api.post_new_user(json.dumps({"pseudo": data.get("email").split('.')[0],
                                                                         "mail": data.get("email"),
                                                                         "password": data.get("password")}))

            else:
                user_bc = self.__boomcraft_api.connect(data.get("email"), data.get("password"))
            if user_bc is None or user_bc[0] >= 400:
                return "Error"
            user_bc_data: dict = user_bc[1]
            user_bc_data.update({"token": user_data.get("token")})
            return user_bc_data

        if user is None or user[0] >= 400:
            return "Error"
        return user[1]

    def __check_if_user_exist(self, user_mail: str = "", user_id: int = -1):
        code = None
        if user_mail:
            code = self.__boomcraft_api.get_user_by_mail(user_mail)
        elif user_id > 0:
            code = self.__boomcraft_api.get_user_by_id(user_id)
        if code is None or code[0] >= 400:
            return False
        return True


    def __get_own_resources(self, id_player):
        resources = self.__boomcraft_api.get_resources_by_id(id_player)
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

    def import_resources(self, id_user, game_resources: dict):
        player: Player = self.__dictionary_player.get_by_id(id_user)
        p_model: PlayerInfoModel = player.model_player
        for _game_res in p_model.game_resources:
            _game_res.quantity = game_resources.get(_game_res.resource, 0)
        for _own_res in p_model.own_resources:
            _own_res.quantity = _own_res.quantity - game_resources.get(_own_res.resource, 0)
        return p_model

    def get_flappy_resources(self, id_flappy, token):
        resources_flappy = self.__flappy_api.get_resources(id_flappy, token)
        if resources_flappy is None or resources_flappy[0] >= 400:
            return {}
        resources = {}
        for _resources in resources_flappy[1].get("ressources"):
            resources.update({_resources.get("ressourceType").get("name"): _resources.get("amount")})
        return resources

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

    def set_resources_end_game(self, winner_id, looser_id):
        winner: Player = self.__dictionary_player.get_by_id(winner_id)
        winner_m: PlayerInfoModel = winner.model_player
        looser: Player = self.__dictionary_player.get_by_id(looser_id)
        looser_m: PlayerInfoModel = looser.model_player

        pack_looser = {}
        for _game_res_loose in looser_m.game_resources:
            pack_looser.update({_game_res_loose.resource: _game_res_loose.quantity})
            _game_res_loose.quantity = 0
        for _game_res_win in winner_m.game_resources:
            _game_res_win.quantity += pack_looser.get(_game_res_win.resource, 0)

        return winner_m, looser_m

    def export_resources(self, player_model):
        resource = {}
        for _resources in player_model.game_resources:
            resource.update({_resources.id_res: _resources.quantity})
        for _resources in player_model.own_resources:
            quantity = _resources.quantity + resource.get(_resources.id_res, 0)
            self.__boomcraft_api.update_resource_by_id(_resources.id_res, quantity)





