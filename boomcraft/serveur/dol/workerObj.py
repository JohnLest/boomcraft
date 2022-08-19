import uuid
import time
import threading
from dol.hitboxObj import HitboxObj
from dol.mobileObj import MobileObj


class WorkerObj(HitboxObj, MobileObj):
    def __init__(self, id_owner, x: int, y: int, width: int = 16, height: int = 32, attack : int = 10, life : int = 100):
        HitboxObj.__init__(self, x, y, width, height)
        MobileObj.__init__(self)
        self.id = str(uuid.uuid4())
        self.id_owner: int = id_owner
        self.life = life
        self.attack: int = attack
        self.is_farming = False
        self.farm_thread = None
        self.cooldown_attack = 1
        self.cooldown_construct = 60
        self.waiting_cooldown = False
        self.price = {"food": 500, "gold": 50}

    def __wait_cooldown(self, cooldown):
        self.waiting_cooldown = True
        time.sleep(cooldown)
        self.waiting_cooldown = False

    def start_cooldown(self, cooldown):
        wait_cooldown = threading.Thread(target=self.__wait_cooldown, args=(cooldown,))
        wait_cooldown.start()
