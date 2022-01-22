

import time
from typing import Dict, List, TYPE_CHECKING

from pygame.sprite import Sprite as Spr

from Worker import WORKER

if TYPE_CHECKING:
    from Party import Party

COULEUR_BLEUE = 0, 0, 255


MAX_WIDTH_SIZE = 840
MAX_HEIGTH_SIZE = 540

# ----------------
#
# class GameEngine
#
# ----------------
class GameEngine():

    def __init__(self, width: int = MAX_WIDTH_SIZE, height: int = MAX_HEIGTH_SIZE) :

        self.__width = width
        """ The play board width """

        self.__height = height
        """ The play board  height"""

        self.__party_nb = 0
        """ The next number available to assign to a new party """

        self.__parties : Dict[int,Party] = None 
        """ The existing parties  """

    def run(self):
        print ("Starting " + self.thread_id)

        for worker in self.workers : 
            print ("prrrt")
            self.move_mobile(worker)
        
        print ("Exiting " + self.thread_id)

    def update_road_to_destination(self,mobile : WORKER) :
        ''' 
        update the road to follow the shorter path
        '''
        mobile.current_step=[mobile.x,mobile.y]

        if(mobile.destination !=[]) :
            while ( mobile.destination != mobile.current_step) :
                self.find_path(mobile)
                time.sleep(1)

    def move_mobile(self,mobile : WORKER) :
        ''' 
        make mobile entity move of one step 
        '''
        if(mobile.road_to_destination != [[]]) :
            mobile.x += mobile.road_to_destination[0][0] 
            mobile.y += mobile.road_to_destination[0][1]
            self.update_gui(mobile.id,mobile.road_to_destination[0], mobile.road_to_destination[1])
            mobile.road_to_destination[0].pop(0)

    def update_gui (self, mobile_id : int, x_move : int, y_move : int, direction : int) : 
        

    def find_path (self, mobile : WORKER):
        """ 
        f(n) = g(n) + h(n) is the minimum cost since the initial node to the objectives conditioned to go thought node n.
        g(n) is the minimum cost from the initial node to n.
        h(n) is the minimum cost from n to the closest objective to n 
        
        In order to choose which square to move to next, we need to take into account 2 heuristics:
            1. The "g" value - This is how far away this node is from the departure point.
            2. The "h" value - This is how far away this node is from the destination point.
            3. The "f" value - This is the sum of the "g" value and the "h" value. 
                        This is the final number which tells us which node to move to.
        
        In order to calculate these heuristics, this is the formula we will use: 
        distance = abs(from.x - to.x) + abs(from.y - to.y)
        
        This is known as the "Manhattan Distance" formula.
        """
        possibility = [[]]
        departure = [mobile.x,mobile.y]


        if (mobile.x > 0) :
            possibility.append([departure[0]-1,departure[1],0]) 
            # as long as mobile.x is greater than 0, it can move to the left (-1,0)

        if(mobile.y+mobile.height < MAX_HEIGTH_SIZE) :
            possibility.append([departure[0],departure[1]+1])
            # as long as mobile.y+mobile.height is smaller than MAX_HEIGTH_SIZE, it can move to the bottom (0,+1)

        if(mobile.y+mobile.height < MAX_HEIGTH_SIZE & mobile.x > 0) :
            possibility.append([departure[0]-1,departure[1]+1])
            # as long as mobile.y+mobile.height is greater than MAX_HEIGTH_SIZE and mobile.x is greater than 0, it can move to the bottom left (-1,+1)

        if (mobile.y > 0) :
            possibility.append([departure[0],departure[1]-1])
            # as long as mobile.y is greater than 0, it can move to the top (0,-1)
        if(mobile.x+mobile.width < MAX_WIDTH_SIZE) :
            possibility.append([departure[0]+1,departure[1]])
            # as long as mobile.x+mobile.width is smaller than MAX_WIDTH_SIZE, it can move to the right (+1,0)

        if(mobile.x+mobile.width < MAX_WIDTH_SIZE & mobile.y > 0) :
            possibility.append([departure[0]+1,departure[1]-1])
            # as long as mobile.x+mobile.width is smaller than MAX_WIDTH_SIZE and mobile.y is greater than 0, it can move to the top right (+1,-1)

        if (mobile.y > 0 & mobile.x > 0) :
            possibility.append([departure[0]-1,departure[1]-1])
            # as long as mobile.x is greater than 0 and mobile.y is greater than 0, it can move to the top left (-1,-1)

        if (mobile.x+mobile.width < MAX_WIDTH_SIZE & mobile.y+mobile.height < MAX_HEIGTH_SIZE) :
            # as long as mobile.x+mobile.width is smaller than MAX_WIDTH_SIZE and mobile.y+mobile.height is smaller than MAX_HEIGTH_SIZE , it can move to the bottom right (+1,0)
            possibility.append([departure[0]+1,departure[1]+1])

        print("possibility")
        self.print_list (possibility)


        f=0
        shortest = []

        possibility = [e for e in possibility if e]
        print("allo possibility")
        self.print_list (possibility)
        

        for position in possibility:
            print("departure")

            self.print_list (departure)
            print("position")
            self.print_list (position)
           
            g = abs(departure[0] - position[0]) + abs(departure[1] - position[1])
            h = abs(position[0] - mobile.destination[0]) + abs(position[1] - mobile.destination[1])
            fbis=g+h

            print("g???", g)
            print("h???", h)
            print("fbis???", fbis)

            if(f == 0 or f>fbis) :
                f=fbis
                ''' 
                 we keep the lowest f value
                '''

                shortest=position
                '''
                then assign case with lowest f to shortest list ([x,y])
                '''
        
        print("avant", mobile.current_step[0], mobile.current_step[1])
            
        print("shortest")
        self.print_list (shortest)

        mobile.current_step[0]+=shortest[0]
        mobile.current_step[1]+=shortest[1]


        print("après",mobile.current_step[0], mobile.current_step[1])

        mobile.road_to_destination.append(shortest)
        ''' 
        once it's added we do the same from the next point (and at the end, we will have the complete road to reach the destination )
        '''




    ################################################################
    #  Getters and Setters
    ################################################################

    def set__width(self, width : int):
        self.__width = width

    def get__width(self) :
        return self.__width

    def set__height(self, height : int):
        self.__height = height

    def get__height(self) :
        return self.__height

    def set__party_nb(self, party_nb : int):
        self.__party_nb = party_nb

    def get__party_nb(self) :
        return self.__party_nb



    def print_list(self,list : list) :
        print(' '.join(map(str, list)))