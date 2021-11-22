from app.game_entity.Character import *

from interface import implements, Interface

class TrainerInterface(Interface):

    def train(self, characterType):
        pass

    def appear_next_to(self):
        pass