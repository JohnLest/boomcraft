import unittest

from app.game_entity.Entity import Entity
from app.game_entity.Ressource import RessourceType
from app.game_entity.Character import Worker

class TestEntity(unittest.TestCase):
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