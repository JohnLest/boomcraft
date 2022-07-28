class Hitbox:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x: int = x
        self.y: int = y
        self.width = width
        self.height = height
        self.hitbox_area_x = [0, 0]
        self.hitbox_area_y = [0, 0]

    def set_hitbox(self):
        self.hitbox_area_x[0] = self.x
        self.hitbox_area_x[1] = self.x + self.width
        self.hitbox_area_y[0] = self.y
        self.hitbox_area_y[1] = self.y + self.height

    def collision(self, hitbox):
        if (
                self.hitbox_area_x[1] > hitbox.hitbox_area_x[0]
                # X max de worker est plus grand que X min de forum
                and
                self.hitbox_area_x[0] < hitbox.hitbox_area_x[1]
                # X min de worker est plus petit que X max de forum
                and
                self.hitbox_area_y[1] > hitbox.hitbox_area_y[0]
                # Y max de worker est plus grand que Y min de forum
                and
                self.hitbox_area_y[0] < hitbox.hitbox_area_y[1]
                # Y min de worker est plus petit que Y max de forum
        ): return True
        return False

