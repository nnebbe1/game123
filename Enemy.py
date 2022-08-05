import pygame as pg
import random
from helper import *
import Environment
import Grid
import math 

vec = pg.math.Vector2

# this class implements the Enemy class, a pigeon, and its movement towards the player
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
        self.pos = vec(random.choice([(-10,-10), (WIDTH /2, -10), (WIDTH, -10), (WIDTH/2, HEIGHT +10), (WIDTH+10, HEIGHT /2)]))
        self.rect.center = (self.pos.x, self.pos.y)
        self.grid_pos = vec(int(self.pos.x / 32), int(self.pos.y / 32))
        self.grid = Grid.Grid(1)
        self.next_grid_step = None
    
    def update(self):
        '''
            A function to update the Enemy --> moves after the player
        '''
        self.next_grid_step = A_Search(self)
        self.move_towards_player()
            
    def set_speed(self, speed):
        '''
            Sets the Enemy's speed

            Parameters:
                speed(int): the wanted speed

        '''
        self.speed = speed

    def heuristic_function(self,grid_node:tuple)->int:
        '''
        Heuristic function that is used in the A* Search


        Parameters:
                self(Enemy) : The pigeon
                grid_node(int tupel): the x and y coord of a grid node

        Returns:
                The euclidian distance between the pigeon 
                and the player character in the grid
                
        '''
        x_coord, y_coord = grid_node
        x_distance = int(abs(x_coord - self.player.grid_pos.x))+1
        y_distance = int(abs(y_coord - self.player.grid_pos.y))+1
        return int(math.sqrt(x_distance*x_distance + y_distance*y_distance))

    
    def move_towards_player(self):

        '''
        Moves the pigeon towards the player along a vector, once a path an a next step has been determined
        Is used in the update function of the Enemy class
        
        Parameters:
                self(Enemy) : The pigeon
            
                
        '''
        # Find direction vector (dx, dy) between enemy and the next step towards the player
        next_step_coords = vec(self.next_grid_step[0] * 32, self.next_grid_step[1] * 32)

        dirvect = vec(next_step_coords.x - self.rect.x,
                                      next_step_coords.y - self.rect.y)
        # scale to speed to keeps speed stead
        try:
            dirvect.normalize()
            dirvect.scale_to_length(self.speed)
        except:
            pass
        #set looking direction accoring to moving direction
        if dirvect.x < 0:
            self.image = pg.image.load('data\images\pigeon_left.png')
        else: 
            self.image = pg.image.load('data\images\pigeon_right.png')

        # Move along this normalized vector towards the next step at current speed.
        self.pos = self.pos + vec(dirvect.x, dirvect.y) 
        self.grid_pos = vec(int(self.pos.x / 32), int(self.pos.y / 32))       
        self.rect.midbottom = self.pos
                
                
                
                
