import pygame as pg
from helper import *

vec = pg.math.Vector2

class Fireball(pg.sprite.Sprite):
    def __init__(self, player):
        '''
            Initialises an object bof the class Fireball

            Parameters:
                player(obj):  the player is needed to know where and in which direction the Fireball is shot
        '''
        pg.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pg.Surface((14,14))
        self.image.fill(LIGHTBLUE)
        pg.draw.circle(self.image, ORANGE, (7,7), 7)
        self.rect = self.image.get_rect()
        
        if player.looking_dir == "right":
            self.vel = vec(5,-1)
            self.pos = vec(self.player.pos.x + 20, self.player.pos.y-15)
        elif player.looking_dir == "left":
            self.vel = vec(-5,-1)
            self.pos = vec(self.player.pos.x - 20, self.player.pos.y-15)

    def update(self):
        '''
            Updates the Fireball by letting it fall less horizontally and more vertically
        '''
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