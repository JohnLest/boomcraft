import unittest

from app.game_entity.Mobile import Mobile
from app.game_entity.Ressource import RessourceType
from app.game_structure.Direction import Direction

class TestMobile(unittest.TestCase):

   def test_move(self) : 
      """ 
      Test that the mobile entity from a to b 
      """

      """ mobileTest = Mobile(RessourceType.WORKER,[0,1],1,2,100,"../resources/worker.png",RessourceType.IRON)

      mobileTest.move(Direction.UP)

      self.assertEqual(mobileTest.get_life(),45) 
      """