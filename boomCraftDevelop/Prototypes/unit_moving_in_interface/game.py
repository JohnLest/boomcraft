from typing import Dict
import pygame
from pygame.locals import *
from Worker import WORKER
from Party import Party

from GameEngine import GameEngine

pygame.init()

map_file = 'BoomCraft_map.png'
character_file = './split/down/1.png'
""" character_file = './split/otherCharacter_0_0.png' """
MAX_WIDTH_SIZE = 840
MAX_HEIGTH_SIZE = 540

SCREEN_SIZE = (MAX_WIDTH_SIZE,MAX_HEIGTH_SIZE)
#opening of the window
screen = pygame.display.set_mode(SCREEN_SIZE)


#load the map
map = pygame.image.load(map_file)
screen.blit(map, (0,0))

#create brain
ge : GameEngine = GameEngine(MAX_WIDTH_SIZE,MAX_HEIGTH_SIZE)
#create a worker
worker : WORKER = WORKER(0,0,0)
worker_position = worker.img.get_rect(topleft=(worker.x, worker.y))

#create dict of workers
workers : Dict[int, WORKER] = {}
surfaces : Dict[int, Rect] = {}

#add one to the dict
workers[0] = worker
surfaces[0] = worker_position

#create a party with workers
party : Party = Party(1, ge,workers)
party.start()
#load the character
#character = pygame.image.load(character_file).convert_alpha()

screen.blit(worker.img, worker_position)

pygame.display.flip()

def receive (self, mobile_id : int, x_move : int, y_move : int, direction : int) :
        workers[mobile_id].x += x_move 
        workers[mobile_id].y += y_move
        surfaces[mobile_id].move(x_move,y_move) 
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            party.game_over=True
            pygame.quit()

        '''        
        if event.type == KEYDOWN:
            if event.key == K_UP:
                worker_position = worker_position.move(0,-5)

            if event.key == K_DOWN:
                worker_position = worker_position.move(0,5)

            if event.key == K_LEFT:
                worker_position = worker_position.move(-5,0)

            if event.key == K_RIGHT:
                worker_position = worker_position.move(5,0) 
        '''

        if (event.type == MOUSEBUTTONDOWN and event.button == 1) :
            print("++++++++++++++++++++++++++++++++++++++++++++")
            print("X : " + str(event.pos[0]) +" / Y : " + str(event.pos[1]))
            print("++++++++++++++++++++++++++++++++++++++++++++")
            worker.destination=[event.pos[0],event.pos[1]]
            if(party.game_over!=True) :
                ge.update_road_to_destination(worker)

    screen.blit(map, (0,0))	
    screen.blit(worker.img, worker_position)
    #refresh
    pygame.display.flip()