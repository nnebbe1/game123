import pygame as pg
import random
from helper import *

vec = pg.math.Vector2

class Goal(pg.sprite.Sprite):
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('data/images/goal-flag.png')
        self.pos = vec(WIDTH-95, 35)
        self.rect = self.image.get_rect()
        self.rect.center = (-50,-50)  
    
    def update(self):
        pass
        