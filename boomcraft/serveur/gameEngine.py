import threading
import time
import uuid

from gameObjects.worker import Worker
from gameObjects.forum import Forum
from playerRepo import PlayerRepo
from gameObjects.map import Map

MAX_WIDTH_SIZE = 1120
MAX_HEIGTH_SIZE = int((900 / 100) * 80)
HITBOX_OFFSET_BUILDING = 10
HITBOX_OFFSET_WORKER = 5


class GameEngine:
    def __init__(self, connect, width: int = MAX_WIDTH_SIZE, height: int = MAX_HEIGTH_SIZE, ):
        self.__width = width
        self.__height = height
        self.__party_nb = 0
        self.game_lst: dict = {}
        self.player_repo = PlayerRepo()
        self.connect = connect

    # region New Game

    def __game_is_available(self):
        for id_game, user_lst in self.game_lst.items():
            if len(user_lst) < 2:
                return id_game
        return None

    def __new_game(self):
        id_game = str(uuid.uuid4())
        self.game_lst.update({id_game: []})
        thread_game_event = threading.Thread(target=self.__game_event, args=(id_game, ), daemon=True)
        thread_game_event.start()
        return id_game

    def add_player_in_game(self, player):
        id_game = self.__game_is_available()
        if id_game is None:
            id_game = self.__new_game()
        player.id_game = id_game
        self.game_lst.get(id_game).append(player)
        return id_game

    # endregion

    # region move worker
    def update_road_to_destination(self, mobile: Worker, forums):
        '''
        update the road to follow the shorter path
        '''
        mobile.current_step = [mobile.x, mobile.y]
        # self.calculate_hitbox_forum(forums)
        if mobile.destination:
            while mobile.destination != mobile.current_step and mobile.destination != []:
                # if forums.life > 0:
                #    self.check_hitbox_reached(mobile, forums, player)
                self.find_path(mobile)
                self.move_mobile(mobile)
                time.sleep(0.001)

    def move_mobile(self, mobile: Worker):
        '''
        make mobile entity move of one step
        '''

        if (mobile.road_to_destination != [[]]):
            mobile.x += mobile.road_to_destination[0][0]
            mobile.y += mobile.road_to_destination[0][1]

            direction: int = 0
            if (mobile.road_to_destination[0] == [0, 1]):
                direction = 1
            elif (mobile.road_to_destination[0] == [0, -1]):
                direction = 2
            elif (mobile.road_to_destination[0] == [1, 0]):
                direction = 3
            elif (mobile.road_to_destination[0] == [-1, 0]):
                direction = 4
            elif (mobile.road_to_destination[0] == [1, 1]):
                direction = 5
            elif (mobile.road_to_destination[0] == [-1, -1]):
                direction = 6
            elif (mobile.road_to_destination[0] == [-1, 1]):
                direction = 7
            elif (mobile.road_to_destination[0] == [1, -1]):
                direction = 8

            # self.calculate_hitbox_mobile(mobile)
            mobile.set_hitbox()
            for id_player, player in self.player_repo.lst_player.items():
                if id_player == mobile.id_owner:
                    self.update_gui(player.id_game)
                    break

            mobile.road_to_destination.pop(0)

            if ([mobile.x, mobile.y] == mobile.destination):
                mobile.destination = []

    def find_path(self, mobile: Worker):
        """
        f(n) = g(n) + h(n) is the minimum cost since the initial node to the objectives conditioned to go thought node n.
        g(n) is the minimum cost from the initial node to n.
        h(n) is the minimum cost from n to the closest objective to n

        In order to choose which square to move to next, we need to take into account 2 heuristics:
            1. The "g" value - This is how far away this node is from the departure point.
            2. The "h" value - This is how far away this node is from the destination point.
            3. The "f" value - This is the sum of the "g" value and the "h" value.
                        This is the final number which tells us which node to move to.

        In order to calculate these heuristics, this is the formula we will use:
        distance = abs(from.x - to.x) + abs(from.y - to.y)

        This is known as the "Manhattan Distance" formula.
        """
        possibility = [[]]
        offsets = [[]]

        departure = [mobile.x, mobile.y]

        offsets = [e for e in offsets if e]

        if (mobile.x > 0):
            possibility.append([departure[0] - 1, departure[1]])
            offsets.append([-1, 0])
            # as long as mobile.x is greater than 0, it can move to the left (-1,0)

        if (mobile.y + mobile.height < self.__height):
            possibility.append([departure[0], departure[1] + 1])
            offsets.append([0, 1])
            # as long as mobile.y+mobile.height is smaller than MAX_HEIGTH_SIZE, it can move to the bottom (0,+1)

        if (mobile.y + mobile.height < self.__height & mobile.x > 0):
            possibility.append([departure[0] - 1, departure[1] + 1])
            offsets.append([-1, 1])
            # as long as mobile.y+mobile.height is greater than MAX_HEIGTH_SIZE and mobile.x is greater than 0, it can move to the bottom left (-1,+1)

        if (mobile.y > 0):
            possibility.append([departure[0], departure[1] - 1])
            offsets.append([0, -1])
            # as long as mobile.y is greater than 0, it can move to the top (0,-1)
        if (mobile.x + mobile.width < self.__width):
            possibility.append([departure[0] + 1, departure[1]])
            offsets.append([1, 0])
            # as long as mobile.x+mobile.width is smaller than MAX_WIDTH_SIZE, it can move to the right (+1,0)

        if (mobile.x + mobile.width < self.__width & mobile.y > 0):
            possibility.append([departure[0] + 1, departure[1] - 1])
            offsets.append([1, -1])
            # as long as mobile.x+mobile.width is smaller than MAX_WIDTH_SIZE and mobile.y is greater than 0, it can move to the top right (+1,-1)

        if (mobile.y > 0 & mobile.x > 0):
            possibility.append([departure[0] - 1, departure[1] - 1])
            offsets.append([-1, -1])
            # as long as mobile.x is greater than 0 and mobile.y is greater than 0, it can move to the top left (-1,-1)

        if (mobile.x + mobile.width < self.__width & mobile.y + mobile.height < self.__height):
            # as long as mobile.x+mobile.width is smaller than MAX_WIDTH_SIZE and mobile.y+mobile.height is smaller than MAX_HEIGTH_SIZE , it can move to the bottom right (+1,0)
            possibility.append([departure[0] + 1, departure[1] + 1])
            offsets.append([1, 1])

        f = 0
        shortest = []
        chosen_move = []
        possibility = [e for e in possibility if e]

        counter: int = -1
        for position in possibility:

            counter += 1

            fbis = self.calculate_f_value(departure, position, mobile.destination)

            if (f == 0 or f > fbis):
                f = fbis
                ''' 
                 we keep the lowest f value
                '''
                chosen_move = offsets[counter]
                shortest = position
                '''
                then assign case with lowest f to shortest list ([x,y])
                '''
        mobile.current_step[0] += chosen_move[0]
        mobile.current_step[1] += chosen_move[1]

        mobile.road_to_destination = [e for e in mobile.road_to_destination if e]

        mobile.road_to_destination.append(chosen_move)

        ''' 
        once it's added we do the same from the next point (and at the end, we will have the complete road to reach the destination )
        '''

    def calculate_f_value(self, departure, position, destination):

        if (departure != [] or position != [] or destination != []):
            g = abs(departure[0] - position[0]) + abs(departure[1] - position[1])
            h = abs(position[0] - destination[0]) + abs(position[1] - destination[1])

            return g + h

    # endregion

    # region Forum
    """"
    def calculate_hitbox_mobile(self, mobile: Worker):

        mobile.hitbox_area_x[0] = mobile.x - HITBOX_OFFSET_WORKER
        mobile.hitbox_area_x[1] = mobile.x + HITBOX_OFFSET_WORKER + mobile.width
        mobile.hitbox_area_y[0] = mobile.y - HITBOX_OFFSET_WORKER
        mobile.hitbox_area_y[1] = mobile.y + HITBOX_OFFSET_WORKER + mobile.height

    def calculate_hitbox_forum(self, forum: Forum):

        forum.hitbox_area_x[0] = forum.x - HITBOX_OFFSET_BUILDING
        forum.hitbox_area_x[1] = forum.x + HITBOX_OFFSET_BUILDING + forum.width

        forum.hitbox_area_y[0] = forum.y - HITBOX_OFFSET_BUILDING
        forum.hitbox_area_y[1] = forum.y + HITBOX_OFFSET_BUILDING + forum.height
    """

    """"
    def check_hitbox_reached(self, attacker: Worker, forum: Forum, key_socket):
        if (
                attacker.hitbox_area_x[1] > forum.hitbox_area_x[0]
                # X max de worker est plus grand que X min de forum
                and
                attacker.hitbox_area_x[0] < forum.hitbox_area_x[1]
                # X min de worker est plus petit que X max de forum
                and
                attacker.hitbox_area_y[1] > forum.hitbox_area_y[0]
                # Y max de worker est plus grand que Y min de forum
                and
                attacker.hitbox_area_y[0] < forum.hitbox_area_y[1]
                # Y min de worker est plus petit que Y max de forum
        ):
            self.attack(attacker, forum, key_socket)
        """

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

    def update_gui(self, id_game):
        all_worker = {}
        for player in self.game_lst.get(id_game):
            for worker in player.workers:
                all_worker.update({worker.id_worker: {"owner": worker.id_owner, "x": worker.x, "y": worker.y}})
        self.connect.send_all({500: all_worker})

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


    # region Getters and Setters



    # endregion
