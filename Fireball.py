import pygame as pg
from helper import *

vec = pg.math.Vector2

class Fireball(pg.sprite.Sprite):
    def __init__(self, player) -> None:
        pg.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pg.Surface((10,10))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.pos = vec(self.player.pos.x + 20, self.player.pos.y-20)
        if player.looking_dir == "right":
            self.vel = vec(5,-1)
        elif player.looking_dir == "left":
            self.vel = vec(-5,-1)

    def update(self):
        if self.vel.x > 0:
            self.vel -= vec(0.05, -0.03)
        elif self.vel.x < 0:
            self.vel += vec(0.05,+0.03)
        elif self.vel.x == 0:
            self.vel.y += 0.05
        if self.pos.y > HEIGHT:
            self.kill()    

        self.pos += self.vel
        self.rect.midbottom = self.pos