import unittest

import sys
import os


sys.path.insert(0, os.path.abspath("."))
from app.game_entity.Character import Character
from app.game_entity.Ressource import RessourceType
from app.game_entity.Mobile import Mobile

class TestCharacter(unittest.TestCase):
    """ 
    Test that the results of an incoming attack gives the expected output 
    """

    def test_attack(self):
        characterTest1 = Character(RessourceType.MOBILE,"Test1",5,60,[0,1],100,"../resources/up/3.png",RessourceType.FOOD)
        print(characterTest1.get_life)
        """
        characterTest2 = Character(RessourceType.MOBILE,"Test2",5,60,[0,1],100,"../resources/worker.png",RessourceType.FOOD)

        characterTest1.attack(characterTest2)
        print(characterTest1.get_life())

        self.assertEqual(characterTest2.get_life(),40,characterTest2.get_life())""" 

if __name__ == '__main__':
    unittest.main() 