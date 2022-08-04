import pygame as pg
import random
import Player
from helper import *
import Environment
import Grid
import math 

vec = pg.math.Vector2

# this class implements the Enemy class, a pigeon, and its movement towards the player
class Enemy(pg.sprite.Sprite):
    
    def __init__(self, player):
        pg.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pg.image.load('data\images\pigeon_left.png')
        self.rect = self.image.get_rect()
        self.speed = 2
        self.pos = vec(WIDTH/2 + 200, HEIGHT/2+100)
        self.rect.center = (self.pos.x, self.pos.y )
        self.grid_pos = vec(int(self.pos.x / 32), int(self.pos.y / 32))
        self.grid = Grid.Grid(1)
        self.next_grid_step = None
    
    def update(self):
        self.grid_pos = vec(int(self.pos.x / 32), int(self.pos.y / 32))
        self.next_grid_step = A_Search(self)
        self.move_towards_player()
        #hits = pg.sprite.spritecollide(self, self.environment.all_platforms, False)
        #if hits:
         #   self.speed = -self.speed
            
    def set_speed(self, speed):
        self.speed = speed

    def heuristic_function(self,grid_node:tuple)->int:
        x_coord, y_coord = grid_node
        x_distance = int(abs(x_coord - self.player.grid_pos.x))+1
        y_distance = int(abs(y_coord - self.player.grid_pos.y))+1
        return int(math.sqrt(x_distance*x_distance + y_distance*y_distance))

    
    def move_towards_player(self):
        # Find direction vector (dx, dy) between enemy and the next step towards the player
        next_step_coords = vec(self.next_grid_step[0] * 32, self.next_grid_step[1] * 32)

        dirvect = pg.math.Vector2(next_step_coords.x - self.rect.x,
                                      next_step_coords.y - self.rect.y)
        dirvect.normalize()
        if dirvect.y > 0:
            self.image = pg.image.load('data\images\pigeon_left.png')
        else: 
            self.image = pg.image.load('data\images\pigeon_right.png')

        # Move along this normalized vector towards the next step at current speed.
        dirvect.scale_to_length(self.speed)
        self.rect.move_ip(dirvect)
        self.pos = vec(self.rect.x, self.rect.y)            
                
                
                
                
                
                
