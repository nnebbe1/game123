import pygame as pg
import random
from helper import *

class Butterfly(pg.sprite.Sprite):
    
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('data/images/Butterfly.png')
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
      
    
    def update(self):
        pass
        
        
    
        
        
        