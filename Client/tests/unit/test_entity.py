import unittest

from app.game_entity.Entity import Entity
from app.game_entity.Ressource import RessourceType

""" 
https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual
 """
class TestApp(unittest.TestCase):

   def test_reduce_life(self) : 
      """ 
      Test that the results of an incoming attack gives the expected output 
      """

      entityTest = Entity([0,1],1,2,100,"olacabzon",RessourceType.FOOD)

      entityTest.reduce_life(55)

      self.assertEqual(entityTest.get_life(),45)


   def test_inactiveAppearance(self) : 
      """ 
      Test that the boolean disapear is set to true 
      """

      entityTest = Entity([0,1],1,2,100,"olacabzon",RessourceType.FOOD)

      entityTest.inactive_appeareance()

      self.assertEqual(entityTest.get_disappear(),True)


   def test_giveArea(self) : 
      """ 
        
      Test that the returned value is correct
        
      """
      entityTest = Entity([0,1],5,8,100,"../resources/forum.png",RessourceType.WOOD)

      self.assertEqual(entityTest.give_area(),40)

   def test_get_width(self) : 
      """ 
        
      Test that the return value is correct
        
      """

      entityTest = Entity([0,1],5,8,100,"../resources/forum.png",RessourceType.WOOD)

      self.assertEqual(entityTest.get_width(),5)

   def test_get_height(self) : 
      """ 
        
      Test that the return value is correct
        
      """
      entityTest = Entity([0,1],5,8,100,"../resources/forum.png",RessourceType.WOOD)

      self.assertEqual(entityTest.get_height(),8)

   def test_isRessourceTypeExists(self) : 
      """ 
        
      Test that the RessourceType entered is recognized
        
      """

      """    
      -----------------------------------------     
      ressourceToCheck

      Ressource instance RessourceType 

      *****self.assertEqual(ressource.getRessourceType(),[25,15])
      """

   def test_giveRessources(self) : 
      """ 
        
      Test that the amount of ressources to give is well given
        
      """

      """    entityTest = Entity([0,1],1,2,100,"Gerard Menvuca",RessourceType.FOOD)

      entityTest.give_ressources(RessourceType.FOOD, 50)

      self.assertEqual(entityTest.get_disappear(),True)
      """

      """    
      -----------------------------------------     
      amount
        
      RessourceCounter instance 

      quantityBeforeTest = getQuantity(RessourceType)

      test

      quantityAfterTest = getQuantity(RessourceType)

      result = quantityAfterTest - quantityBeforeTest

      self.assertTrue(result == amount)
      """



if __name__ == '__main__':
    unittest.main()