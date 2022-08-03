import pygame as pg
import random
from helper import *




class Enemy(pg.sprite.Sprite):
    
    def __init__(self, player):
        '''
            Initialises an object of class Enemy
            
            Parameters:
                player(obj): the player the enemy has as its target
                
        '''
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
        '''
            A function to update the Enemy --> moves after the player
        '''

        self.move_towards_player()
            
    def set_speed(self, speed):
        '''
            Sets the Enemy's speed

            Parameters:
                speed(int): the wanted speed

        '''
        self.speed = speed
        