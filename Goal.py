import pygame as pg
import random
from helper import *

vec = pg.math.Vector2

#this class implements the goal flag that can be reached by the player to win the game

class Goal(pg.sprite.Sprite):
    
    def __init__(self):
        """
        Initialises a object of class Goal
        """
    
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('data/images/goal-flag.png')
        self.pos = vec(WIDTH-95, 35)
        self.rect = self.image.get_rect()
        self.rect.center = (-50,-50)  
    
    def update(self):
        pass
        