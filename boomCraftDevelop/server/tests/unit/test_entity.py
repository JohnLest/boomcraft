import unittest
import sys


from server.app.game_entity.Entity import Entity
from server.app.game_entity.Ressource import RessourceType

class TestEntity(unittest.TestCase):

   def test_reduce_life(self) : 
      """ 
      Test that the results of an incoming attack gives the expected output 
      """

      entityTest = Entity([0,1],1,2,100,"app/resources/down/0.png",RessourceType.FOOD)

      entityTest.reduce_life(55)

      self.assertEqual(entityTest.get_life(),45)


   def test_inactiveAppearance(self) : 
      """ 
      Test that the boolean disapear is set to true 
      """

      entityTest = Entity([0,1],1,2,100,"app/resources/down/0.png",RessourceType.FOOD)

      entityTest.inactive_appeareance()

      self.assertEqual(entityTest.get_disappear(),True)


   def test_giveArea(self) : 
      """ 
        
      Test that the returned value is correct
        
      """
      entityTest = Entity([0,1],5,8,100,"app/resources/down/0.png",RessourceType.WOOD)

      self.assertEqual(entityTest.give_area(),40)

   def test_get_width(self) : 
      """ 
        
      Test that the return value is correct
        
      """

      entityTest = Entity([0,1],5,8,100,"app/resources/down/0.png",RessourceType.WOOD)

      self.assertEqual(entityTest.get_width(),5)

   def test_get_height(self) : 
      """ 
        
      Test that the return value is correct
        
      """
      entityTest = Entity([0,1],5,8,100,"app/resources/down/0.png",RessourceType.WOOD)
      self.assertEqual(entityTest.get_height(),8)

   def test_isRessourceTypeExists(self) : 
      """ 
        
      Test that the RessourceType entered is not recognized
        
      """
      entityTest = Entity([0,1],5,8,100,"app/resources/down/0.png","henri")
      value = entityTest.get_ressource_dropped()
      mustReturnFalse = isinstance(value, RessourceType)
      self.assertEqual(mustReturnFalse,False)






if __name__ == '__main__':
    unittest.main()