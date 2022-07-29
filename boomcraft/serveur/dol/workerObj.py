import uuid
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
