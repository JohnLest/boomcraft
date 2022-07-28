import time
import threading

from dol.workerObj import WorkerObj as Worker
from dol.dictionaryObj import DictionaryObj

class WorkerService:
    def __init__(self):
        self.dictionary_worker = DictionaryObj()
        self.stop_farm = True
        self.is_farming = False
        self.farm_resource_thread = threading.Thread()

    def create_worker(self, id_user, x_work, y_work):
        new_worker = Worker(id_user, x=x_work, y=y_work)
        self.dictionary_worker.insert(new_worker.id_worker, new_worker)
        return

    def get_all_workers_by_id_player(self, id_player):
        return self.dictionary_worker.get_all_filter("id_owner", id_player)

    def get_worker_by_id(self, id_worker):
        return self.dictionary_worker.get_by_id(id_worker)

    def set_new_destination(self, id_worker, destination):
        worker: Worker = self.dictionary_worker.get_by_id(id_worker)
        worker.destination = [destination[0], destination[1]]

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
