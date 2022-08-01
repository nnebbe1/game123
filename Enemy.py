import pygame as pg
import random
import Player
from helper import *
import Environment



class Enemy(pg.sprite.Sprite):
    
    def __init__(self, player):
        pg.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pg.image.load('data\images\pigeon_left.png')
        self.rect = self.image.get_rect()
        self.speed = 2
        self.rect.y = random.randint(0, HEIGHT) 
        self.rect.x = random.choice([-350, -100, -75, -50, WIDTH+50, WIDTH+75, WIDTH+100])
        
    def move_towards_player(self):
        # Find direction vector (dx, dy) between enemy and player.
        player_pos = self.player.get_pos()
        dirvect = pg.math.Vector2(player_pos[0] - self.rect.x,
                                      player_pos[1] - self.rect.y)
        dirvect.normalize()
        if dirvect.y > 0:
            self.image = pg.image.load('data\images\pigeon_left.png')
        else: 
            self.image = pg.image.load('data\images\pigeon_right.png')
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self.speed)
        self.rect.move_ip(dirvect)
    
      
    
    def update(self):
        self.move_towards_player()
        #hits = pg.sprite.spritecollide(self, self.environment.all_platforms, False)
        #if hits:
         #   self.speed = -self.speed
            
    def set_speed(self, speed):
        self.speed = speed
        