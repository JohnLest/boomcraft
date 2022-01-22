
################################################################
# PYGAME LINKED CLASSES
################################################################

from typing import List
import pytmx
from pygame.sprite import Group, Sprite
from pygame import Rect, Surface
import pygame, random, sys

class Level(object):
    def __init__(self, file_name):

         #Create map object from PyTMX
        self.mapObject = pytmx.load_pygame(file_name)
        
        # Create list of layers for map
        self.layers : List[Layer] = [] 
        
        #Amount of level shift left/right
        self.levelShift : int = 0 
        
        #Create layers for each layer in tile map
        for layer in range(len(self.mapObject.layers)):
            self.layers.append(Layer(index = layer, mapObject = self.mapObject))
    
    #Move layer left/right
    def shiftLevel(self, shiftX):
        self.levelShift += shiftX
        
        for layer in self.layers:
            for tile in layer.tiles:
                tile.rect.x += shiftX
    
    #Update layer
    def draw(self, screen):
        for layer in self.layers:
            layer.draw(screen)
            
class Layer(object):
    def __init__(self, index, mapObject):
        #Layer index from tiled map
        self.index = index
        
        #Create group of tiles for this layer
        self.tiles = Group()
        
        #Reference map object
        self.mapObject = mapObject
        
        #Create tiles in the right position for each layer
        for x in range(self.mapObject.width):
            for y in range(self.mapObject.height):
                img = self.mapObject.get_tile_image(x, y, self.index)
                if img:
                    self.tiles.add(Tile(image = img, x = (x * self.mapObject.tilewidth), y = (y * self.mapObject.tileheight)))

    #Draw layer
    def draw(self, screen):
        self.tiles.draw(screen)

class Tile(Sprite):
    ''' 
    Tile class with an image, x and y 
    '''
    def __init__(self, image, x, y):
        Sprite.__init__(self)
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class SpriteSheet(object):
    ''' 
    Sprite sheet class to load sprites from player spritesheet 
    '''
    def __init__(self, file_name):
        self.sheet = pygame.image.load(file_name)

    def image_at(self, rectangle):
        rect = Rect(rectangle)
        image = Surface(rect.size, pygame.SRCALPHA, 32).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        return image