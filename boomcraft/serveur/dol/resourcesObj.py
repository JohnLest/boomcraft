from dol.hitboxObj import HitboxObj


class ResourcesObj(HitboxObj):
    def __init__(self, type, x, y, width, height):
        super().__init__(x, y, width, height)
        self.type = type
