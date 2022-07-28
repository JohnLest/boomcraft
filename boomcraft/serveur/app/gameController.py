import time

from dol.workerObj import WorkerObj as Worker
from dol.forumObj import Forum
from bll.services.playerService import PlayerService
from bll.services.gameService import GameService
from bll.services.workerService import WorkerService
from bll.services.mobileService import MobileService
from dol.mapObj import Map


class GameController:
    def __init__(self, connect):
        self.player_service = PlayerService()
        self.game_service = GameService()
        self.worker_service = WorkerService()
        self.mobile_service = MobileService()
        self.connect = connect

        # TODO to remove :
        self.forum = Forum(600, 600)

    def new_player(self, key_socket, **data):
        model_player = self.player_service.new_player(key_socket, **data)
        to_send = model_player.dict()
        to_send.pop("key_socket")
        self.connect.write(key_socket, {1: to_send})
        return model_player.user.id_user

    def update_resources(self, id_user, game_resources):
        model_player = self.player_service.update_resources(id_user, game_resources)
        to_send = model_player.dict()
        to_send.pop("key_socket")
        self.connect.write(self.player_service.get_socket(id_user), {2: to_send})
        return model_player.user.id_user

    def add_player_game(self, id_user):
        id_game = self.game_service.add_player_in_game(id_user)
        self.connect.write(self.player_service.get_socket(id_user), {3: {"id_game": id_game}})

    def create_worker(self, id_user, id_game):
        size_game = self.game_service.get_size_game(id_game)
        if size_game == 1:
            self.worker_service.create_worker(id_user, 100, 100)
        elif size_game == 2:
            self.worker_service.create_worker(id_user, 500, 500)
        self.update_gui(id_game)

    def move_worker(self, id_worker, destination):
        self.worker_service.set_new_destination(id_worker, destination)
        worker = self.worker_service.get_worker_by_id(id_worker)
        id_game = self.game_service.get_id_game_with_player(worker.id_owner)
        self.update_road_to_destination(id_game, worker, None)

    def update_road_to_destination(self, id_game, mobile, forums):
        '''
        update the road to follow the shorter path
        '''
        mobile.current_step = [mobile.x, mobile.y]
        # self.calculate_hitbox_forum(forums)
        if mobile.destination:
            while mobile.destination != mobile.current_step and mobile.destination != []:
                # if forums.life > 0:
                #    self.check_hitbox_reached(mobile, forums, player)
                self.mobile_service.find_path(mobile)
                self.mobile_service.move_mobile(mobile)
                self.update_gui(id_game)
                time.sleep(0.001)


    def update_gui(self, id_game):
        all_worker = {}
        list_socket = []
        for id_player in self.game_service.get_player_in_game(id_game):
            list_socket.append(self.player_service.get_socket(id_player))
            for worker in self.worker_service.get_all_workers_by_id_player(id_player):
                all_worker.update({worker.id_worker: {"owner": id_player, "x": worker.x, "y": worker.y}})
        for socket in list_socket:
            self.connect.write(socket, {500: all_worker})



    # region Forum

    def attack(self, attacker: Worker, forum: Forum, key_socket):
        print("avant forum.life --> ", forum.life)
        forum.life = forum.life - attacker.attack

        if (forum.life <= 0):
            print("Forum est détruit")
            self.connect.write(key_socket, {501: {"vie Forum": False}})
        elif (forum.life > 0):
            print(f"Le forum a une vie de {forum.life}")
        time.sleep(0.5)

    # endregion



    def __game_event(self, id_game):
        map = Map()
        while True:
            self.__check_worker_collision(id_game, map)

    def __check_worker_collision(self, id_game, map):
        for player in self.game_lst.get(id_game):
            for worker in player.workers:
                pass
                # self.__worker_farm_resources(worker, map)

    def __worker_farm_resources(self, worker, map):
        for _hitbox_tree in map.lst_trees:
            if worker.collision(_hitbox_tree):
                if not worker.is_farming:
                    worker.is_farming = True
                    worker.farm_resources("trees")
                return
        for _hitbox_stone in map.lst_stone:
            if worker.collision(_hitbox_stone):
                if not worker.is_farming:
                    worker.is_farming = True
                    worker.farm_resources("stone")
                return
        for _hitbox_ore in map.lst_ore:
            if worker.collision(_hitbox_ore):
                if not worker.is_farming:
                    worker.is_farming = True
                    worker.farm_resources("ore")
                return
        worker.is_farming = False
        worker.farm_resources(None)

