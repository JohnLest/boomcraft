import time
import threading
import logging

from bll.services.playerService import PlayerService
from bll.services.gameService import GameService
from bll.services.itemService import ItemService
from bll.services.mobileService import MobileService


class GameController:
    def __init__(self, connect):
        self.logger = logging.getLogger(__name__)
        self.player_service = PlayerService()
        self.game_service = GameService()
        self.item_service = ItemService()
        self.mobile_service = MobileService()
        self.connect = connect

    def new_player(self, key_socket, **data):
        model_player = self.player_service.new_player(key_socket, **data)
        if model_player is None:
            self.logger.warning(f" No users found ")
            self.connect.write(key_socket, {1: None})
            return None
        to_send = model_player.dict()
        to_send.pop("key_socket")
        self.logger.info(f"Send message - key : 1 ")
        self.connect.write(key_socket, {1: to_send})
        return model_player.user.id_user

    def update_resources(self, id_user, game_resources):
        model_player = self.player_service.update_resources(id_user, game_resources)
        to_send = model_player.dict()
        to_send.pop("key_socket")
        self.logger.info(f"Send message - key : 2 ")
        self.connect.write(self.player_service.get_socket(id_user), {2: to_send})
        return model_player.user.id_user

    def add_boss_game(self, id_game):
        game = self.game_service.get_game(id_game)
        if game.boss is None:
            boss = self.item_service.create_boss(name="saint")
            game.boss = boss

    def add_player_game(self, id_user):
        id_game = self.game_service.add_player_in_game(id_user)
        self.add_boss_game(id_game)
        self.logger.info(f"Send message - key : 3 ")
        self.connect.write(self.player_service.get_socket(id_user), {3: {"id_game": id_game}})
        if self.game_service.get_thread_game_event(id_game) is None:
            thread_game_event = threading.Thread(target=self.__game_event, args=(id_game, ), daemon=True)
            self.game_service.set_thread_game_event(id_game, thread_game_event)
            thread_game_event.start()

    def init_player_in_gui(self, id_user, id_game):
        size_game = self.game_service.get_size_game(id_game)
        if size_game == 1:
            self.item_service.create_worker(id_user, 100, 100)
            self.item_service.create_forum(id_user, 100, 500)
        elif size_game == 2:
            self.item_service.create_worker(id_user, 1000, 100)
            self.item_service.create_forum(id_user, 1000, 500)
        self.__update_gui(id_game)

    def new_forum(self, id_worker):
        worker = self.item_service.get_worker_by_id(id_worker)
        if worker.waiting_cooldown:return
        player_model = self.player_service.check_if_resource_available(worker.id_owner, {"gold": 500, "iron": 500, "stone": 1000, "wood": 1000, "food": 750})
        if player_model is None: return
        worker.start_cooldown(worker.cooldown_construct)
        self.item_service.create_forum(worker.id_owner, worker.x + 16, worker.y + 32)
        id_game = self.game_service.get_id_game_with_player(worker.id_owner)
        self.__send_info_player(player_model)
        self.__update_gui(id_game)

    def new_worker(self, id_forum):
        forum = self.item_service.get_forum_by_id(id_forum)
        if forum.waiting_cooldown:return
        player_model = self.player_service.check_if_resource_available(forum.id_owner,
                                                                       {"food": 500, "gold": 50})
        if player_model is None: return
        forum.start_cooldown(forum.cooldown_construct)
        self.item_service.create_worker(forum.id_owner, forum.x - 16, forum.y - 32)
        id_game = self.game_service.get_id_game_with_player(forum.id_owner)
        self.__send_info_player(player_model)
        self.__update_gui(id_game)

    def move_worker(self, id_worker, destination):
        self.item_service.set_new_destination(id_worker, destination)
        worker = self.item_service.get_worker_by_id(id_worker)
        id_game = self.game_service.get_id_game_with_player(worker.id_owner)
        self.update_road_to_destination(id_game, worker)

    def update_road_to_destination(self, id_game, mobile):
        '''
        update the road to follow the shorter path
        '''
        mobile.current_step = [mobile.x, mobile.y]
        if mobile.destination:
            while mobile.destination != mobile.current_step and mobile.destination != []:
                save_position = mobile.current_step.copy()
                self.mobile_service.find_path(mobile)
                self.mobile_service.move_mobile(mobile)
                is_collision_enemy = self.item_service.is_collision_with_enemy(mobile.id)
                if is_collision_enemy is not None:
                    mobile.current_step = save_position.copy()
                    mobile.x = mobile.current_step[0]
                    mobile.y = mobile.current_step[1]
                    if not mobile.waiting_cooldown:
                        self.item_service.attack(mobile, is_collision_enemy)
                        mobile.start_cooldown(mobile.cooldown_attack)
                self.__update_gui(id_game)
                time.sleep(0.001)

    def __update_gui(self, id_game):
        all_worker = {}
        all_forum = {}
        list_socket = []
        game = self.game_service.get_game(id_game)
        boss = game.boss
        boss_data = {}
        boss_alive = self.item_service.check_boss_is_alive(boss.id)
        if boss_alive is not None:
            boss_data = {"id_boss": boss.id, "name": boss.name, "x": 0, "y": 0, "life": 0}
        else:
            boss_data = {"id_boss": boss.id, "name": boss.name, "x": boss.x, "y": boss.y, "life": boss.life}
        for id_player in self.game_service.get_player_in_game(id_game):
            list_socket.append(self.player_service.get_socket(id_player))
            if not self.item_service.get_all_forum_by_id_player(id_player):
                game.end_game = True
                game.thread_game_event.join()
                game.thread_game_event = None
            for worker in self.item_service.get_all_workers_by_id_player(id_player):
                is_alive = self.item_service.check_worker_is_alive(worker.id)
                if is_alive is not None:
                    all_worker.update({worker.id: {"owner": id_player, "x": 0, "y": 0, "life": 0}})
                    continue
                all_worker.update({worker.id: {"owner": id_player, "x": worker.x, "y": worker.y}})
            for forum in self.item_service.get_all_forum_by_id_player(id_player):
                is_alive = self.item_service.check_forum_is_alive(forum.id)
                if is_alive is not None:
                    all_forum.update({forum.id: {"owner": id_player, "x": 0, "y": 0, "life": 0}})
                    continue
                all_forum.update({forum.id: {"owner": id_player, "x": forum.x, "y": forum.y, "life": forum.life}})
        for socket in list_socket:
            if not game.end_game:
                self.connect.write(socket, {500: [all_worker, all_forum, boss_data]})
            else:
                self.__end_game(id_game)

                for id, worker in all_worker.items():
                    self.item_service.destroy_worker(id)
                for id, forum in all_forum.items():
                    self.item_service.destroy_forum(id)

    def __game_event(self, id_game):
        map = self.game_service.get_map()
        while True:
            self.__check_worker_collision(id_game, map)
            if self.game_service.get_game(id_game).end_game:
                break

    def __check_worker_collision(self, id_game, map):
        for player_id in self.game_service.get_player_in_game(id_game):
            for worker in self.item_service.get_all_workers_by_id_player(player_id):
                worker_id = worker.id
                type_resource = self.item_service.is_collision_with_resources(worker_id, map)
                if type_resource is not None and not worker.is_farming:
                    farm_resource_thread = threading.Thread(target=self.__thread_farm, args=(worker, type_resource,), daemon=True)
                    self.item_service.set_thread_farm(worker_id, farm_resource_thread)
                    farm_resource_thread.start()
                elif type_resource is None and worker.is_farming:
                    self.item_service.stop_thread_farm(worker_id)

    def __thread_farm(self, worker, resource):
        count = 0
        id_player = self.item_service.get_id_player_by_id_worker(worker.id)
        while True:
            player_model = None
            if resource == "trees":
                time.sleep(1)
                if not worker.is_farming: return
                if count % 5 == 4:
                    player_model = self.player_service.farm_resources(id_player, {"food": 10, "wood": 10})
                else:
                    player_model = self.player_service.farm_resources(id_player, {"wood": 10})
            elif resource == "stone":
                time.sleep(1)
                if not worker.is_farming: return
                player_model = self.player_service.farm_resources(id_player, {"stone": 10})
            elif resource == "ore":
                time.sleep(2)
                if not worker.is_farming: return
                if count % 5 == 4:
                    player_model = self.player_service.farm_resources(id_player, {"gold": 5, "iron": 10})
                else:
                    player_model = self.player_service.farm_resources(id_player, {"iron": 10})
            if not worker.is_farming: return
            if player_model is not None:
                self.__send_info_player(player_model)
            count += 1

    def __send_info_player(self, player_model):
        id_player = player_model.user.id_user
        to_send = player_model.dict()
        to_send.pop("key_socket")
        self.connect.write(self.player_service.get_socket(id_player), {2: to_send})

    def __end_game(self, id_game):
        winner = ""
        looser = ""
        for id_player in self.game_service.get_player_in_game(id_game):
            if self.item_service.get_all_forum_by_id_player(id_player):
                winner = id_player
            else:
                looser = id_player
        if winner == "" or looser == "":
            return
        players_model = self.player_service.set_resources_end_game(winner, looser)
        for player in players_model:
            self.__send_info_player(player)

        self.connect.write(self.player_service.get_socket(winner), {666: "win"})
        self.connect.write(self.player_service.get_socket(looser), {666: "loose"})
        time.sleep(0.01)
