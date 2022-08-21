import uuid

class GameObj:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.players = []
        self.thread_game_event = None
        self.end_game = False
        self.boss = None
        self.rarity_gold = 1
        self.rarity_food = 0

