from app.Sum import Sum


import unittest


class TestApp(unittest.TestCase):

    def test_list_int(self) : 
        """ Test that it can add integer list """
        data = [1,2,3]
        result = Sum.sum(data)

        self.assertEqual(result,6)
        
    def test_alloa(self) : 
        """ Test that it returns vateretrrororo """
        result = Sum.callAlloa()

        self.assertEqual(result,'vateretrrororo')
        
if __name__ == '__main__':
    unittest.main()