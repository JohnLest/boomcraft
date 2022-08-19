from models.playerInfoModel import PlayerInfoModel


class PlayerObj:
    def __init__(self, model_player: PlayerInfoModel):
        self.model_player = model_player
        self.id_game = None
        self.id_workers = []
