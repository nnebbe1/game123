import pygame as pg
from helper import *
vec = pg.math.Vector2

class Platform(pg.sprite.Sprite):
    def __init__(self, grid_x ,grid_y, type):
        '''
            Initialises an object of class Platform
            
            Parameters:
                grid_x(int), grid_y(int): it's coordinates in the grid
                type(str): it's type (solid or not)
        '''
        if type == "solid":
            self.type = "solid"
            pg.sprite.Sprite.__init__(self)
            self.image = pg.image.load("data\images\_Brick.png") 
            self.rect = self.image.get_rect()
            self.gridposition = vec(int(grid_x), int(grid_y))
            self.rect.center = vec((HEIGHT-grid_x*32) +144, (WIDTH-grid_y*32)-144)