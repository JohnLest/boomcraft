import sys, pygame

from pygame.sprite import Sprite as Spr

COULEUR_BLEUE = 0, 0, 255


MAX_WIDTH_SIZE = 840
MAX_HEIGTH_SIZE = 540

CHARACTER_UP = './split/up/0.png'
CHARACTER_DOWN = './split/down/0.png'
CHARACTER_LEFT = './split/left/0.png'
CHARACTER_RIGHT = './split/right/0.png'

# ----------------
#
# class WORKER
#
# ----------------
class WORKER(Spr):


    def __init__(self) :
        super(Spr).__init__(self)
        self.rect.x = 0
        self.rect.y = 0
        self.width = 16
        self.height = 32

        self.img_up = pygame.image.load(CHARACTER_UP).convert_alpha()
        self.img_down = pygame.image.load(CHARACTER_DOWN).convert_alpha()
        self.img_left = pygame.image.load(CHARACTER_LEFT).convert_alpha()
        self.img_right = pygame.image.load(CHARACTER_RIGHT).convert_alpha()
        self.img = self.img_up
        self.destination = []
        """ 
        The destination to arrive to

        self.rect.x = 9
        self.rect.y = 25

        example --> [15,25]
        or
        example --> [13,22]

        """
        self.road_to_destination = [[]]
        """ 
        The points on which mobile has to pass to arrive to the destination
        self.rect.x = 9
        self.rect.y = 25
        example --> [[10,25], [11,25], [12,25], [13,25], [14,25], [15,25]]
        or              X,Y
        example --> [[1,-1],[1,-1],[1,-1],[1,0]]

        """
        self.DEPLACEMENT = 1

    def update(self) :

        if(self.destination !=[]) :
            while ( self.destination not in self.road_to_destination) :
                self.find_path()
                
            if(self.road_to_destination != [[]]) :
                self.rect.x += self.road_to_destination[0][0] 
                self.rect.y += self.road_to_destination[0][1]
                self.road_to_destination[0].pop(0)



    def find_path (self):
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
        departure = [self.rect.x, self.rect.y]

        if (self.rect.x > 0) :
            possibility.append([departure[0]-1,departure[1],0])

        if(self.rect.y+self.height < MAX_HEIGTH_SIZE) :
            possibility.append([departure[0],departure[1]+1,1])

        if(self.rect.y+self.height < MAX_HEIGTH_SIZE & self.rect.x > 0) :
            possibility.append([departure[0]-1,departure[1]+1,2])

        if (self.rect.y > 0) :
            possibility.append([departure[0],departure[1]-1,3])

        if(self.rect.x+self.width < MAX_WIDTH_SIZE) :
            possibility.append([departure[0]+1,departure[1],4])

        if(self.rect.x+self.width < MAX_WIDTH_SIZE & self.rect.y > 0) :
            possibility.append([departure[0]+1,departure[1]-1,5])

        if (self.rect.y > 0 & self.rect.x > 0) :
            possibility.append([departure[0]-1,departure[1]-1,6])

        if (self.rect.x+self.width < MAX_WIDTH_SIZE & self.rect.y+self.height < MAX_HEIGTH_SIZE) :
            possibility.append([departure[0]+1,departure[1]+1,7])
            
        f=0
        shortest = []

        for possi in possibility:
            g = abs(departure[0] - possi[0]) + abs(departure[1] - possi[1])
            h = abs(possi[0] - self.destination[0]) + abs(possi[1] - self.destination[1])
            fbis=g+h

            if(f == 0 | f>fbis) :
                f=fbis
                shortest=possi

        self.road_to_destination.append(shortest)

        """ if (shortest[2] ==  0) :
            self.road_to_destination.append([-1,0])
        elif (shortest[2] ==  1) :
            self.road_to_destination.append([0,+1])
        elif (shortest[2] ==  2) :
            self.road_to_destination.append([-1,+1])
        elif (shortest[2] ==  3) :
            self.road_to_destination.append([0,-1])
        elif (shortest[2] ==  4) :
            self.road_to_destination.append([+1,0])
        elif (shortest[2] ==  5) :
            self.road_to_destination.append([+1,-1])
        elif (shortest[2] ==  6) :
            self.road_to_destination.append([-1,-1])
        elif (shortest[2] ==  7) :
            self.road_to_destination.append([+1,+1])
        else : 
            print("there is problem with the path") 
        """


        """
        Let's calculate the "g" value for the blue square immediately to the left of the green square: abs(3 - 2) + abs(2 - 2) = 1
        Great! We've got the value: 1. Now, let's try calculating the "h" value: abs(2 - 0) + abs(2 - 0) = 4
        Perfect. Now, let's get the "f" value: 1 + 4 = 5
        So, the final value for this node is "5".
        Let's do the same for all the other blue squares. The big number in the center of each square is the "f" value, while
        the number on the top left is the "g" value, and the number on the top right is the "h" value:
        """
   

# ----------------
#
# Code
#
# ----------------
pygame.init()
screen = pygame.display.set_mode((400, 400))
background = pygame.Surface(screen.get_size())
background.fill(COULEUR_BLEUE)
screen.blit(background, (0, 0))

pygame.display.set_caption("Le carré qui rebondit")

clock = pygame.time.Clock()

XX = 300
DEPLACEMENT = 0.2

all_sprites = pygame.sprite.Group()
carre = CARRE()
all_sprites.add(carre)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    all_sprites.clear(screen, background)
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
