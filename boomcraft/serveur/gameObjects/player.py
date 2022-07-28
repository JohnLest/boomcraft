from typing import List
from gameObjects.worker import Worker
from models.playerInfoModel import PlayerInfoModel


class Player:
    def __init__(self, model_player: PlayerInfoModel):
        self.workers: List[Worker] = []
        self.forum = None
        self.model_player = model_player
        self.id_game = None
