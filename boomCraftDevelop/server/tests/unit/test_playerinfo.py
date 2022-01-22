import unittest

""" 
https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual
 """
class TestApp(unittest.TestCase):

    def test_updateOwnRessources(self) : 
        """ 
        
        Test that the global ressources owner is well updated 
        
        """
        """ 
        -----------------------------------------
        ownRessources instance RessourceCounter

        gameRessources instance RessourceCounter

        self.assertEqual(gameRessources.getQuantity(),1500)
        
        """


    def test_importFromOwnRessources(self) : 
        """ 
        
        Test that the game ressources 
        has the good quantities for each resources
        following what is filled in the form
        
        """

        """ 
        -----------------------------------------

        List[int]

        ownRessources instance RessourceCounter

        gameRessources instance RessourceCounter

        self.assertEqual(ownRessources.getQuantity(),1500)

        self.assertEqual(gameRessources.getQuantity(),200)
        """

    def test_dontexceedmaxpossiblequantity(self) : 
        """ 
        
        Test that the quantity entered in form doesn't exceed the maximal POSSIBLE quantity
        
        """

        """    
        -----------------------------------------     
        self.assertTrue(0 < ownRessources.getQuantity())
        """

    def test_dontexceedmaxpermittedquantity(self) : 
        """ 
        
        Test that the quantity entered in form doesn't exceed the maximal PERMITTED quantity
        
        """

        """    
        -----------------------------------------     
        self.assertTrue(varMaxQuantity >= gameRessources.getQuantity())
        """

    def test_ownandgameressourcesarenotequalafterinitialization(self) : 
        """ 
        
        Test ownRessources and gameRessources are not equal after initialization
        
        """
        """ 

        -----------------------------------------
        ownRessources instance RessourceCounter

        gameRessources instance RessourceCounter

        self.assertNotEqual(gameRessources,ownRessources)

        List[resources]
        
        """



if __name__ == '__main__':
    unittest.main()