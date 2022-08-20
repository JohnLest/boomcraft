import json
import time
import threading
import logging

from apis.flappyApi import FlappyApi
from bll.services.playerService import PlayerService
from bll.services.gameService import GameService
from bll.services.itemService import ItemService
from bll.services.mobileService import MobileService


class GameController:
    def __init__(self, connect, boomcraft_api, pong_api, flappy_api):
        self.__logger = logging.getLogger(__name__)
        self.__boomcraft_api = boomcraft_api
        self.__pong_api = pong_api
        self.__flappy_api: FlappyApi = flappy_api
        self.__player_service = PlayerService(self.__boomcraft_api, self.__pong_api, self.__flappy_api)
        self.__game_service = GameService(self.__boomcraft_api)
        self.__item_service = ItemService(self.__boomcraft_api)
        self.__mobile_service = MobileService()
        self.__connect = connect

    def new_player(self, key_socket, **data):
        model_player = self.__player_service.new_player(key_socket, **data)
        if model_player is None:
            self.__logger.warning(f" No users found ")
            self.__connect.write(key_socket, {1: None})
            return None
        to_send = model_player.dict()
        to_send.pop("key_socket")
        self.__logger.info(f"Send message - key : 1 ")
        self.__connect.write(key_socket, {1: to_send})
        return model_player.user.id_user

    def update_resources(self, id_user, game_resources):
        model_player = self.__player_service.import_resources(id_user, game_resources)
        to_send = model_player.dict()
        to_send.pop("key_socket")
        self.__logger.info(f"Send message - key : 2 ")
        self.__connect.write(self.__player_service.get_socket(id_user), {2: to_send})
        return model_player.user.id_user

    def add_boss_game(self, id_game):
        game = self.__game_service.get_game(id_game)
        if game.boss is None:
            boss = self.__item_service.create_boss()
            game.boss = boss

    def add_player_game(self, id_user):
        id_game = self.__game_service.add_player_in_game(id_user)
        self.add_boss_game(id_game)
        self.__logger.info(f"Send message - key : 3 ")
        self.__connect.write(self.__player_service.get_socket(id_user), {3: {"id_game": id_game}})
        if self.__game_service.get_thread_game_event(id_game) is None:
            thread_game_event = threading.Thread(target=self.__game_event, args=(id_game, ), daemon=True)
            self.__game_service.set_thread_game_event(id_game, thread_game_event)
            thread_game_event.start()

    def init_player_in_gui(self, id_user, id_game):
        size_game = self.__game_service.get_size_game(id_game)
        if size_game == 1:
            self.__item_service.create_worker(id_user, 100, 100)
            self.__item_service.create_forum(id_user, 100, 500)
        elif size_game == 2:
            self.__item_service.create_worker(id_user, 1000, 100)
            self.__item_service.create_forum(id_user, 1000, 500)
        self.__update_gui(id_game)

    def new_forum(self, id_worker):
        worker = self.__item_service.get_worker_by_id(id_worker)
        if worker.waiting_cooldown:return
        player_model = self.__player_service.check_if_resource_available(worker.id_owner, {"gold": 500, "iron": 500, "stone": 1000, "wood": 1000, "food": 750})
        if player_model is None: return
        worker.start_cooldown(worker.cooldown_construct)
        self.__item_service.create_forum(worker.id_owner, worker.x + 16, worker.y + 32)
        id_game = self.__game_service.get_id_game_with_player(worker.id_owner)
        self.__send_info_player(player_model)
        self.__update_gui(id_game)

    def new_worker(self, id_forum):
        forum = self.__item_service.get_forum_by_id(id_forum)
        if forum.waiting_cooldown:return
        player_model = self.__player_service.check_if_resource_available(forum.id_owner,
                                                                         {"food": 500, "gold": 50})
        if player_model is None: return
        forum.start_cooldown(forum.cooldown_construct)
        self.__item_service.create_worker(forum.id_owner, forum.x - 16, forum.y - 32)
        id_game = self.__game_service.get_id_game_with_player(forum.id_owner)
        self.__send_info_player(player_model)
        self.__update_gui(id_game)

    def move_worker(self, id_worker, destination):
        self.__item_service.set_new_destination(id_worker, destination)
        worker = self.__item_service.get_worker_by_id(id_worker)
        id_game = self.__game_service.get_id_game_with_player(worker.id_owner)
        self.update_road_to_destination(id_game, worker)

    def update_road_to_destination(self, id_game, mobile):
        '''
        update the road to follow the shorter path
        '''
        mobile.current_step = [mobile.x, mobile.y]
        if mobile.destination:
            while mobile.destination != mobile.current_step and mobile.destination != []:
                save_position = mobile.current_step.copy()
                self.__mobile_service.find_path(mobile)
                self.__mobile_service.move_mobile(mobile)
                is_collision_enemy = self.__item_service.is_collision_with_enemy(mobile.id)
                if is_collision_enemy is not None:
                    mobile.current_step = save_position.copy()
                    mobile.x = mobile.current_step[0]
                    mobile.y = mobile.current_step[1]
                    if not mobile.waiting_cooldown:
                        bonus_dead = self.__item_service.attack(mobile, is_collision_enemy)
                        if bonus_dead :
                            self.__kill_enemy(mobile.id_owner, bonus_dead)
                        mobile.start_cooldown(mobile.cooldown_attack)
                self.__update_gui(id_game)
                time.sleep(0.001)

    def get_flappy_resources(self, id_player):
        player = self.__player_service.get_player_by_id(id_player).model_player
        if player.user.token =="": return
        player_flappy = self.__flappy_api.get_player_exist(player.user.mail, player.user.token)
        if player_flappy is None or player_flappy[0] >= 400: return
        resource = self.__player_service.get_flappy_resources(player_flappy[1].get("id"), player.user.token)
        resource.update({"Gold": 0})
        for name, val in resource.items():
            if name == "Diamond":
                resource.update({"Gold": resource.get("Gold", 0) + val * 5})

        self.__connect.write(self.__player_service.get_socket(id_player), {103: resource})

    def transfer_flappy_resources(self, resource: dict):
        player = self.__player_service.get_player_by_id(resource.get("id_user")).model_player
        if player.user.token == "": return
        resource.pop("id_user")
        player_flappy = self.__flappy_api.get_player_exist(player.user.mail, player.user.token)
        if player_flappy is None or player_flappy[0] >= 400: return
        _resource = self.__player_service.get_flappy_resources(player_flappy[1].get("id"), player.user.token)
        resource_list = self.__flappy_api.get_resource_list(player.user.token)
        for name, val in _resource.items():
            to_remove = resource.get(name, 0)
            if name == "Diamond":
                to_remove = int(resource.get("Gold", 0) / 5 + 0.9)

            for res_type in resource_list[1].get("ressourceTypesList"):
                if res_type.get("name") == name:
                    if to_remove > 0:
                        self.__flappy_api.remove_resources(player.user.token, json.dumps({"idPlayer": player_flappy[1].get("id"),
                                                                                     "idRessourceType": res_type.get("id"),
                                                                                     "amountToDelete": to_remove}))

        for key in resource.keys():
            resource[key.lower()] = resource.pop(key)

        player_model = self.__player_service.farm_resources(player.user.id_user, resource)
        self.__send_info_player(player_model)


    def __kill_enemy(self, id_user, bonus_dead):
        p_model = self.__player_service.farm_resources(id_user, bonus_dead)
        self.__send_info_player(p_model)

    def __update_gui(self, id_game):
        all_worker = {}
        all_forum = {}
        list_socket = []
        game = self.__game_service.get_game(id_game)
        boss = game.boss
        boss_data = {}
        boss_alive = self.__item_service.check_boss_is_alive(boss.id)
        if boss_alive is not None:
            boss_data = {"id_boss": boss.id, "name": boss.name, "x": 0, "y": 0, "life": 0}
        else:
            boss_data = {"id_boss": boss.id, "name": boss.name, "x": boss.x, "y": boss.y, "life": boss.life}
        for id_player in self.__game_service.get_player_in_game(id_game):
            list_socket.append(self.__player_service.get_socket(id_player))
            if not self.__item_service.get_all_forum_by_id_player(id_player):
                game.end_game = True
                game.thread_game_event.join()
                game.thread_game_event = None
            for worker in self.__item_service.get_all_workers_by_id_player(id_player):
                is_alive = self.__item_service.check_worker_is_alive(worker.id)
                if is_alive is not None:
                    all_worker.update({worker.id: {"owner": id_player, "x": 0, "y": 0, "life": 0}})
                    continue
                all_worker.update({worker.id: {"owner": id_player, "x": worker.x, "y": worker.y}})
            for forum in self.__item_service.get_all_forum_by_id_player(id_player):
                is_alive = self.__item_service.check_forum_is_alive(forum.id)
                if is_alive is not None:
                    all_forum.update({forum.id: {"owner": id_player, "x": 0, "y": 0, "life": 0}})
                    continue
                all_forum.update({forum.id: {"owner": id_player, "x": forum.x, "y": forum.y, "life": forum.life}})
        for socket in list_socket:
            if not game.end_game:
                self.__connect.write(socket, {500: [all_worker, all_forum, boss_data]})
            else:
                self.__end_game(id_game)

                for id, worker in all_worker.items():
                    self.__item_service.destroy_worker(id)
                for id, forum in all_forum.items():
                    self.__item_service.destroy_forum(id)

    def __game_event(self, id_game):
        map = self.__game_service.get_map()
        while True:
            self.__check_worker_collision(id_game, map)
            if self.__game_service.get_game(id_game).end_game:
                break

    def __check_worker_collision(self, id_game, map):
        for player_id in self.__game_service.get_player_in_game(id_game):
            for worker in self.__item_service.get_all_workers_by_id_player(player_id):
                worker_id = worker.id
                type_resource = self.__item_service.is_collision_with_resources(worker_id, map)
                if type_resource is not None and not worker.is_farming:
                    farm_resource_thread = threading.Thread(target=self.__thread_farm, args=(worker, type_resource,id_game,), daemon=True)
                    self.__item_service.set_thread_farm(worker_id, farm_resource_thread)
                    farm_resource_thread.start()
                elif type_resource is None and worker.is_farming:
                    self.__item_service.stop_thread_farm(worker_id)

    def __thread_farm(self, worker, resource, id_game):
        count = 0
        id_player = self.__item_service.get_id_player_by_id_worker(worker.id)
        game = self.__game_service.get_game(id_game)
        while True:
            player_model = None
            if resource == "trees":
                time.sleep((4 * game.rarity_food) + 1)
                if not worker.is_farming: return
                if count % 5 == 4:
                    player_model = self.__player_service.farm_resources(id_player, {"food": 10, "wood": 10})
                else:
                    player_model = self.__player_service.farm_resources(id_player, {"wood": 10})
            elif resource == "stone":
                time.sleep(1)
                if not worker.is_farming: return
                player_model = self.__player_service.farm_resources(id_player, {"stone": 10})
            elif resource == "ore":
                time.sleep((2 * (game.rarity_gold * 10)) + 1)
                if not worker.is_farming: return
                if count % 5 == 4:
                    player_model = self.__player_service.farm_resources(id_player, {"gold": 5, "iron": 10})
                else:
                    player_model = self.__player_service.farm_resources(id_player, {"iron": 10})
            if not worker.is_farming: return
            if player_model is not None:
                self.__send_info_player(player_model)
            count += 1

    def __send_info_player(self, player_model):
        id_player = player_model.user.id_user
        to_send = player_model.dict()
        to_send.pop("key_socket")
        self.__connect.write(self.__player_service.get_socket(id_player), {2: to_send})

    def __end_game(self, id_game):
        winner = ""
        looser = ""
        for id_player in self.__game_service.get_player_in_game(id_game):
            if self.__item_service.get_all_forum_by_id_player(id_player):
                winner = id_player
            else:
                looser = id_player
        if winner == "" or looser == "":
            return
        players_model = self.__player_service.set_resources_end_game(winner, looser)
        for player in players_model:
            self.__player_service.export_resources(player)
            self.__send_info_player(player)

        self.__connect.write(self.__player_service.get_socket(winner), {666: "win"})
        self.__connect.write(self.__player_service.get_socket(looser), {666: "loose"})
        time.sleep(0.01)
