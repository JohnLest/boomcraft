import time
import threading

from tool import *
from apis.boomcraftApi import BoomcraftApi
from apis.otherApi import *
from dol.workerObj import WorkerObj as Worker
from dol.forumObj import ForumObj as Forum
from dol.bossObj import BossObj as Boss
from dol.dictionaryObj import DictionaryObj
from tool import *

class ItemService:
    def __init__(self, boomcraft_api):
        self.__dictionary_worker = DictionaryObj()
        self.__dictionary_forum = DictionaryObj()
        self.__dictionary_boss = DictionaryObj()
        self.__boomcraft_api: BoomcraftApi = boomcraft_api
        self.__stop_farm = True
        self.__farm_resource_thread = threading.Thread()
        self.is_farming = False

    def create_boss(self):
        name = self.__get_name_saint()
        new_boss = Boss(name, 255, 255)
        new_boss.set_hitbox()
        self.__dictionary_boss.insert(new_boss.id, new_boss)
        return new_boss

    def create_worker(self, id_user, x_work, y_work):
        new_worker = Worker(id_user, x=x_work, y=y_work)
        new_worker.set_hitbox()
        self.__dictionary_worker.insert(new_worker.id, new_worker)
        return

    def get_all_workers_by_id_player(self, id_player):
        return self.__dictionary_worker.get_all_filter("id_owner", id_player)

    def get_id_player_by_id_worker(self, id_worker):
        return first_or_default(self.__dictionary_worker.get_attribute("id_owner", "id", id_worker))

    def get_worker_by_id(self, id_worker):
        return self.__dictionary_worker.get_by_id(id_worker)

    def get_forum_by_id(self, id_forum):
        return self.__dictionary_forum.get_by_id(id_forum)

    def set_new_destination(self, id_worker, destination):
        worker: Worker = self.__dictionary_worker.get_by_id(id_worker)
        worker.destination = [destination[0], destination[1]]

    def is_collision_with_resources(self, id_worker, map):
        worker: Worker = self.__dictionary_worker.get_by_id(id_worker)
        for _hitbox_tree in map.lst_trees:
            if worker.collision(_hitbox_tree):
                return "trees"
        for _hitbox_stone in map.lst_stone:
            if worker.collision(_hitbox_stone):
                return "stone"
        for _hitbox_ore in map.lst_ore:
            if worker.collision(_hitbox_ore):
                return "ore"
        return None

    def is_collision_with_enemy(self, id_worker):
        worker: Worker = self.__dictionary_worker.get_by_id(id_worker)
        for _key, _forum in self.__dictionary_forum.get_all().items():
            if worker.collision(_forum) and worker.id_owner != _forum.id_owner:
                return _forum

        for _key, _worker in self.__dictionary_worker.get_all().items():
            if worker.collision(_worker) and worker.id_owner != _worker.id_owner:
                return _worker

        for _key, _boss in self.__dictionary_boss.get_all().items():
            if worker.collision(_boss):
                return _boss

        return None

    def set_thread_farm(self, id_worker, thread):
        worker: Worker = self.__dictionary_worker.get_by_id(id_worker)
        worker.farm_thread = thread
        worker.is_farming = True

    def stop_thread_farm(self, id_woker):
        worker: Worker = self.__dictionary_worker.get_by_id(id_woker)
        worker.is_farming = False
        worker.farm_thread.join()
        worker.farm_thread = None

    def create_forum(self, id_player, x, y):
        new_forum = Forum(id_player, x=x, y=y)
        new_forum.set_hitbox()
        self.__dictionary_forum.insert(new_forum.id, new_forum)

    def get_all_forum_by_id_player(self, id_player):
        return self.__dictionary_forum.get_all_filter("id_owner", id_player)

    def attack(self, attacker, defender):
        print(f"attaker attack {attacker.attack} defender {defender.life}")
        defender.life = defender.life - attacker.attack
        if defender.life <= 0:
            return defender.bonus
        return {}

    def check_forum_is_alive(self, id_forum):
        forum: Forum = self.__dictionary_forum.get_by_id(id_forum)
        if forum.life <= 0:
            self.__dictionary_forum.delete(id_forum)
            del forum
            return id_forum
        return None

    def check_worker_is_alive(self, id_worker):
        worker: Worker = self.__dictionary_worker.get_by_id(id_worker)
        if worker.life <= 0:
            worker.x = 0
            worker.y = 0
            worker.height = 1
            worker.width = 1
            worker.set_hitbox()
            time.sleep(0.01)
            # if worker.is_farming:
            #   self.stop_thread_farm(id_worker)
            self.__dictionary_worker.delete(id_worker)
            del worker
            return id_worker
        return None

    def check_boss_is_alive(self, id_boss):
        boss: Boss = self.__dictionary_boss.get_by_id(id_boss)
        if boss is None: return
        if boss.life <= 0:
            boss.x = 0
            boss.y = 0
            boss.width = 1
            boss.height = 1
            boss.set_hitbox()
            self.__dictionary_boss.delete(id_boss)
            del boss
            return id_boss
        return None

    def destroy_forum(self, id_forum):
        forum: Forum = self.__dictionary_forum.get_by_id(id_forum)
        self.__dictionary_forum.delete(id_forum)
        del forum

    def destroy_worker(self, id_worker):
        worker: Worker = self.__dictionary_worker.get_by_id(id_worker)
        worker.x = 0
        worker.y = 0
        worker.height = 0
        worker.width = 0
        worker.set_hitbox()
        if worker.is_farming:
            self.stop_thread_farm(id_worker)
        self.__dictionary_worker.delete(id_worker)
        del worker

    def __get_name_saint(self):
        uri = "https://nominis.cef.fr/json"
        request = "saintdujour.php"
        saint = get_request(uri, request)
        full_name = saint.get("response").get("saintdujour").get("nom")
        name_split = full_name.split(' ')
        if len(name_split) > 1:
            return name_split[1]
        return first_or_default(name_split)
