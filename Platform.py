from telnetlib import XASCII
import pygame as pg
from helper import *
vec = pg.math.Vector2

class Platform(pg.sprite.Sprite):
    def __init__(self, grid_x ,grid_y, type) ->None:
        if type == "solid":
            self.type = "solid"
            pg.sprite.Sprite.__init__(self)
            self.image = pg.image.load("data\images\_Brick.png") 
            self.rect = self.image.get_rect()
            self_gridposition = vec(int(grid_x), int(grid_y))
            self.rect.center = vec((HEIGHT-grid_x*32) +144, (WIDTH-grid_y*32)-144)