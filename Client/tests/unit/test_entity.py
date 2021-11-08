import unittest

""" 
https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual
 """
class TestApp(unittest.TestCase):

    def test_inactiveAppearance(self) : 
        """ 
        
        Test that the boolean disapear is set to true 
        
        """
        """ 
        -----------------------------------------
        entity instance disappear

        self.assertEqual(disappear.get(),true)
        
        """


    def test_defineLookInGame(self) : 
        """ 
        
        Test that the file exist ? 
        
        """

        """ 
        -----------------------------------------
        *** import os.path ***
        FileName

        entity instance lookInGame

        self.assertTrue(os.path.isfile(FileName))

        """

    def test_giveArea(self) : 
        """ 
        
        Test that the return value is correct
        
        """

        """    
        -----------------------------------------     
        entity instance rectangle 

        self.assertEqual(entity.giveArea(),[25,15])
        """

     def test_giveWidth(self) : 
        """ 
        
        Test that the return value is correct
        
        """

        """    
        -----------------------------------------     
        entity instance width 

        self.assertEqual(entity.giveWidth(),20)
        """

     def test_giveHeight(self) : 
        """ 
        
        Test that the return value is correct
        
        """

        """    
        -----------------------------------------     
        entity instance coords 

        self.assertEqual(entity.giveHeight(),15)
        """

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