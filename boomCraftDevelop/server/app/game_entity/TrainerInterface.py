from boomCraftDevelop.server.app.game_entity.Character import *

from interface import implements, Interface

class TrainerInterface(Interface):

    def train(self, character_type):
        pass

    def appear_next_to(self, character_type):
        pass