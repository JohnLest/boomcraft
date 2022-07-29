import uuid
from dol.hitboxObj import HitboxObj as Hitbox


class ForumObj(Hitbox):
    def __init__(self, id_owner, x: int = 0, y: int = 0, width: int = 64, height: int = 64, life: int = 100):
        super().__init__(x, y, width, height)
        self.id = str(uuid.uuid4())
        self.id_owner = id_owner
        self.life = life
