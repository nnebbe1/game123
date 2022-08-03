import pygame as pg
from helper import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    
    def __init__(self, environment,wasd_or_arrow_keys) -> None:
        pg.sprite.Sprite.__init__(self)
        self.environment = environment
        self.wasd_or_arrow_keys = wasd_or_arrow_keys
        self.image = pg.image.load("data\images\dino_right.png")
        self.looking_dir = "right"
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.grid_pos = vec(int(self.pos.x / 32), int(self.pos.y / 32))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.climbing = False

    def jump(self):
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.environment.all_platforms, False)
        self.rect.y -= 1 
        if hits:
            self.vel.y = -PLAYER_JUMP
    


    def update(self):
        #gravity
        self.acc = vec(0,0.2)

        #acceleration left and right when key press
        keys = pg.key.get_pressed()
        if self.wasd_or_arrow_keys == "wasd":
            if keys[pg.K_a]:
                self.image = pg.image.load("data\images\dino_left.png") 
                self.looking_dir = "left"
                self.acc.x = -0.5
            if keys[pg.K_d]:
                self.image = pg.image.load("data\images\dino_right.png") 
                self.looking_dir = "right"
                self.acc.x = 0.5
        elif self.wasd_or_arrow_keys == "arrow":
            if keys[pg.K_LEFT]:
                self.image = pg.image.load("data\images\dino_left.png") 
                self.looking_dir = "left"
                self.acc.x = -0.5
            if keys[pg.K_RIGHT]:
                self.image = pg.image.load("data\images\dino_right.png") 
                self.looking_dir = "right"
                self.acc.x = 0.5

        
        # motion with friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.grid_pos = vec(int(self.pos.x / 32), int(self.pos.y / 32))

        # wrap around the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos
        
    def get_pos(self):
        return self.pos
