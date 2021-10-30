from app.Sum import Sum

""" 

Hello Alloa 

"""
class Alloa():

    age = None # public variable
    _id = 0 # Private variable

    _data = []
    def __init__(self, int1=0, int2=0):
        self.data = [int1,int2]
        print(data)

    """ 
        getter of self.data
    """
    @property
    def listOfInteger(self):
        return self.data

    """ 
        setter
    """
    @data.setter
    def listOfInteger(self,data):
        """ set the data list in data attribute """
        for i in data :
            if not (0 <= data[i] <100):
                raise ValueError(f'Data list ({data[i]}) must be 0-100')
            elif (0 <= data[i] <100):
                self.data = data
                print(data)

    def bitch() :
        return "vateretrrororo"
    def bitchIsCalculating() :
        return Sum.sum(self.data)

