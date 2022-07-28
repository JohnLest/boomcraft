from gameObjects.hitbox import Hitbox


class Resources(Hitbox):
    def __init__(self, type, x, y, width, height):
        super().__init__(x, y, width, height)
        self.type = type
