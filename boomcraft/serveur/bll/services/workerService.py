import time
import threading

from dol.workerObj import WorkerObj as Worker
from dol.dictionaryObj import DictionaryObj
from tool import *

class WorkerService:
    def __init__(self):
        self.__dictionary_worker = DictionaryObj()
        self.stop_farm = True
        self.is_farming = False
        self.farm_resource_thread = threading.Thread()

    def create_worker(self, id_user, x_work, y_work):
        new_worker = Worker(id_user, x=x_work, y=y_work)
        self.__dictionary_worker.insert(new_worker.id_worker, new_worker)
        return

    def get_all_id_workers_by_id_player(self, id_player):
        return self.__dictionary_worker.get_all_filter("id_owner", id_player)

    def get_id_player_by_id_worker(self, id_worker):
        return first_or_default(self.__dictionary_worker.get_attribute("id_owner", "id_worker", id_worker))

    def get_worker_by_id(self, id_worker):
        return self.__dictionary_worker.get_by_id(id_worker)

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

    def set_thread_farm(self, id_worker, thread):
        worker: Worker = self.__dictionary_worker.get_by_id(id_worker)
        worker.farm_thread = thread
        worker.is_farming = True

    def stop_thread_farm(self, id_woker):
        worker: Worker = self.__dictionary_worker.get_by_id(id_woker)
        worker.is_farming = False
        worker.farm_thread.join()
        worker.farm_thread = None

    """"
    def __thread_farm(self, resource):
        count = 0
        while True:
            if resource == "trees":
                time.sleep(1)
                if self.stop_farm: return
                if count % 5 == 4:
                    self.connect.write(self.socket_owner, {4: {"food": 10}})
                self.connect.write(self.socket_owner, {4: {"wood": 10}})
            elif resource == "stone":
                time.sleep(1)
                if self.stop_farm: return
                self.connect.write(self.socket_owner, {4: {"stone": 10}})
            elif resource == "ore":
                time.sleep(2)
                if self.stop_farm: return
                if count % 5 == 4:
                    self.connect.write(self.socket_owner, {4: {"gold": 5}})
                self.connect.write(self.socket_owner, {4: {"iron": 10}})
            if self.stop_farm: return
            count += 1

    def farm_resources(self, resource):
        if self.is_farming:
            self.stop_farm = False
            self.farm_resource_thread = threading.Thread(target=self.__thread_farm, args=(resource,), daemon=True)
            self.farm_resource_thread.start()
            print("start")
        elif not self.is_farming:
            self.stop_farm = True
            self.farm_resource_thread.join()
        print("test")
    """
