import pygame as pg
from helper import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, environment) -> None:
        pg.sprite.Sprite.__init__(self)
        self.environment = environment
        self.image = pg.image.load("data\images\dino_right.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH / 2, HEIGHT-40)
        self.looking_dir = "right"
        self.pos = vec(WIDTH / 2, HEIGHT-40)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.environment.all_platforms, False)
        self.rect.y -= 1 
        if hits:
            self.vel.y = -PLAYER_JUMP
    


    def update(self):

        #acceleration left and right when key press
        self.acc = vec(0,0.2)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.image = pg.image.load("data\images\dino_left.png") 
            self.looking_dir = "left"
            self.acc.x = -0.5
        if keys[pg.K_d]:
            self.image = pg.image.load("data\images\dino_right.png") 
            self.looking_dir = "right"
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

        self.rect.midbottom = self.pos
        
    def get_pos(self):
        return self.pos