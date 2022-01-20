import pygame
from pygame.locals import *

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

#load the character
character = pygame.image.load(character_file).convert_alpha()

character_position = character.get_rect()
screen.blit(character, character_position)


''' def pxToCase (self, x, y) : 

    x%16
    y% 
'''


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                character_position = character_position.move(0,-5)

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                character_position = character_position.move(0,5)

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                character_position = character_position.move(-5,0)

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                character_position = character_position.move(5,0)

        if event.type == MOUSEBUTTONDOWN and event.button == 1 :
    	    print("X : " + str(event.pos[0]) +" / Y : " + str(event.pos[1]))



    screen.blit(map, (0,0))	
    screen.blit(character, character_position)
    #refresh
    pygame.display.flip()