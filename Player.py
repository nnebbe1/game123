import pygame as pg
from helper import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, environment) -> None:
        pg.sprite.Sprite.__init__(self)
        self.environment = environment
        self.icon = pg.image.load("data\pics\dino_right.png")
        self.rect = self.icon.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT /2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.environment.platforms, False)
        self.rect.y -= 1 
        if hits:
            self.vel.y = -10


    def update(self):

        #acceleration left and right when key press
        self.acc = vec(0,0.2)
        keys = pg.key.get_pressed()
<<<<<<< Updated upstream
        if keys[pg.K_a]:
            self.icon = pg.image.load("data\pics\dino_left.png") 
            self.acc.x = -0.5
        if keys[pg.K_d]:
            self.icon = pg.image.load("data\pics\dino_right.png") 
            self.acc.x = 0.5
=======
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

>>>>>>> Stashed changes
        
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