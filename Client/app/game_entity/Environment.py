class Environment :
    
    def __init__(self):
        
            self.active = "boolean"


    """ 
     follow the season by putting a filter on the picture of the entity
    """
    def followSeason(self):
        print("active " + self.active)



class Tree(Environment) :
    
    def __init__(self):
        super(Tree, self).__init__()
