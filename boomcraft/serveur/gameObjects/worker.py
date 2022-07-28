import uuid
import time
import threading
from gameObjects.hitbox import Hitbox


class Worker(Hitbox):
    def __init__(self, connect,  id_owner, socket_owner, x: int, y: int, width: int = 16, height: int = 32, attack : int = 10, life : int = 100):
        super().__init__(x, y, width, height)
        self.connect = connect
        self.socket_owner = socket_owner
        self.id_worker = str(uuid.uuid4())
        self.id_owner: int = id_owner
        self.destination: list[int] = []
        self.road_to_destination = [[]]
        self.current_step: list[int] = []
        self.life = life
        self.attack: int = attack
        self.stop_farm = True
        self.is_farming = False

        self.farm_resource_thread = threading.Thread()

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
