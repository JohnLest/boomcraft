class Forum:
    def __init__(self, x: int = 0, y: int = 0, width: int = 64, height: int = 64, life: int = 100):
        self.x : int = x
        self.y : int = y
        self.width = width
        self.height = height
        self.life = life
        self.hitbox_area_x = [0,0]
        self.hitbox_area_y = [0,0]