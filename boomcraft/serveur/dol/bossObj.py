import uuid
from dol.hitboxObj import HitboxObj


class BossObj(HitboxObj):
    def __init__(self, name, x: int, y: int, width: int = 32, height: int = 32, life: int = 1000):
        HitboxObj.__init__(self, x, y, width, height)
        self.id = str(uuid.uuid4())
        self.life = life
        self.name = name
        self.bonus = {"gold": 500, "iron": 500, "stone": 1000, "wood": 1000, "food": 750}
