class Worker:
    def __init__(self, x: int, y: int, width: int = 16, height: int = 32):
        self.x: int = x
        self.y: int = y
        self.width = width
        self.height = height
        self.destination: list[int] = []
        self.road_to_destination = [[]]
        self.current_step: list[int] = []