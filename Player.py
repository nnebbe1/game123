import pygame as pg
from helper import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        pg.sprite.Sprite.__init__(self)
        
        self.icon = pg.image.load("data\pics\dino_right.png")
        self.rect = self.icon.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT /2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def update(self):

        #acceleration left and right when key press
        self.acc = vec(0,0.1)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.icon = pg.image.load("data\pics\dino_left.png") 
            self.acc.x = -0.5
        if keys[pg.K_d]:
            self.icon = pg.image.load("data\pics\dino_right.png") 
            self.acc.x = 0.5
        
        # motion with friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # wrap around the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.center = self.pos