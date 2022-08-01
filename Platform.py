from telnetlib import XASCII
import pygame as pg
from helper import *
vec = pg.math.Vector2

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, type) ->None:
        if type == "solid":
            self.type = "solid"
            pg.sprite.Sprite.__init__(self)
            self.image = pg.Surface((w,h))
            self.image.fill(BROWN)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        if type == "not_solid":
            self.type = "not_solid"
            pg.sprite.Sprite.__init__(self)
            self.image = pg.Surface((w,h))
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y