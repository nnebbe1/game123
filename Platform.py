from telnetlib import XASCII
import pygame as pg
from helper import *
vec = pg.math.Vector2

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h) ->None:
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y