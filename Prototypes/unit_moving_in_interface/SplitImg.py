from PIL import Image
from itertools import product
import os

def tile(filename, dir_in, dir_out, width, height):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    
    grid = product(range(0, h-h%height, height), range(0, w-w%width, width))
    for i, j in grid:
        box = (j, i, j+width, i+height)
        out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
        img.crop(box).save(out)


tile("otherCharacter.png","./","split/" ,16,16)