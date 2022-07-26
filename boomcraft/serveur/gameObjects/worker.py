import uuid

class Worker:
    def __init__(self, x: int, y: int, width: int = 16, height: int = 32, attack : int = 10, life : int = 100):
        self.id_worker = uuid.uuid4()
        self.x: int = x
        self.y: int = y
        self.width = width
        self.height = height
        self.destination: list[int] = []
        self.road_to_destination = [[]]
        self.current_step: list[int] = []
        self.life = life
        self.hitbox_area_x = [0, 0]
        self.hitbox_area_y = [0, 0]
        self.attack: int = attack
