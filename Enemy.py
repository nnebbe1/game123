import pygame as pg
import random
import Player
from helper import *
import Environment

vec = pg.math.Vector2


class Enemy(pg.sprite.Sprite):
    
    def __init__(self, player):
        pg.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pg.image.load('data\images\pigeon_left.png')
        self.rect = self.image.get_rect()
        self.speed = 2
        self.pos = vec(random.randint(0, HEIGHT),random.choice([-350, -100, -75, -50, WIDTH+50, WIDTH+75, WIDTH+100]))
        self.rect.center = (self.pos.x, self.pos.y )
        self.grid_pos = vec(int(self.pos.x / 32), int(self.pos.y / 32))
        self.current_path = list()
    
    def update(self):
        self.grid_pos = vec(int(self.pos.x / 32), int(self.pos.y / 32))
        self.current_path = self.A_Search()
        self.move_towards_player()
        #hits = pg.sprite.spritecollide(self, self.environment.all_platforms, False)
        #if hits:
         #   self.speed = -self.speed
            
    def set_speed(self, speed):
        self.speed = speed

    def h(self):
        x_distance = abs(self.grid_pos.x - self.player.gird_pos.x)
        y_distance = abs(self.grid_pos.y - self.player.gird_pos.y)
        return x_distance + y_distance

    def A_Search(self):
        # get start and goal from the position of the pigeon and the positon of the player
        start = self.grid_pos
        goal = self.player.grid_pos

        #open list and closed list
        open_lst = {start}
        closed_lst = {}
    
        dists = {}
        dists[start] = 0
    
        path = {}
        path[start] = start
    
        while open_lst: 
            current_node = None
        
            for v in open_lst:
                if current_node == None or dists[v] + self.h(v) < dists[n] + self.h(n):
                    current_node = v
                
            if n == None:
                return None
        
        
            if n == goal:
                reconst_path = []
            
                while path[n] != n:
                    reconst_path.append(n)
                    n = path[n]
                
                reconst_path.append(start)
            
                reconst_path.reverse()
            
                return reconst_path
            
            for m in self.get_neighbors(n):
          # if the current node is not presentin both open_lst and closed_lst
            # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    path[m] = n
                    dists[m] = dists[n] + 1
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if dists[m] > dists[n] + 1:
                        dists[m] = dists[n] + 1
                        path[m] = n
 
                    if m in closed_lst:
                        closed_lst.remove(m)
                        open_lst.add(m)
 
            open_lst.remove(n)
            closed_lst.add(n)
        
        return None

    def move_towards_player(self):
        # Find direction vector (dx, dy) between enemy and the next step towards the player
        next_grid_step = self.current_path[1]
        next_step_coords = vec(next_grid_step.x * 32, next_grid_step.y * 32)

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
                
                
                
                
                
                
