import uuid

class GameObj:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.players = []
        self.thread_game_event = None
