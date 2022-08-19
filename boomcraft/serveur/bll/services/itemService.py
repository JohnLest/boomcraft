import time
import threading

from dol.workerObj import WorkerObj as Worker
from dol.forumObj import ForumObj as Forum
from dol.dictionaryObj import DictionaryObj
from tool import *

class ItemService:
    def __init__(self):
        self.__dictionary_worker = DictionaryObj()
        self.__dictionary_forum = DictionaryObj()
        self.stop_farm = True
        self.is_farming = False
        self.farm_resource_thread = threading.Thread()

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
        defender.life = defender.life - attacker.attack

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
            self.__dictionary_worker.delete(id_worker)
            del worker
            return id_worker
        return None
