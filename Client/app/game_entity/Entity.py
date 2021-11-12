class Entity :
    
    def __init__(self):
        
            self.active = "boolean"

            self.disappear = "boolean"

            self.coords = "List[Coord]"

            self.life = "int"

            self.look_in_game = "String"

            self.ressource_dropped = "RessourceType"


    """ 
     make entity appear inactive
    """
    def inactive_appeareance(self):
        print("active " + self.active)

    """
     define the path to follow to get the entity image
    """
    def define_look_in_game(self, path_to_entity_image):
        print("look_in_game " + self.look_in_game)


    
    def set_active(self,active):
            self.active = active

    def get_active(self):
        return self.active

    def set_active(self,active):
        self.active = active

    def get_active(self):
        return self.active


        