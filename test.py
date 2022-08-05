from asyncore import write
from lib2to3.pgen2.token import NEWLINE
import pygame

import Enemy
import Grid
import Player
import Environment
import helper
import Platform
import random
from helper import *
import time
import csv



def A_Search(self)->tuple:
        # get start and goal from the position of the pigeon and the positon of the player
        start_node = (self.grid_pos.x, self.grid_pos.y)
        goal_node = (self.player.grid_pos.x, self.player.grid_pos.y)

        #open list and closed list
        open_lst = list()
        open_lst.append(start_node)
        closed_lst = list()
    
        dists = {}
        dists[start_node] = 0
    
        path = {}
        path[start_node] = start_node
    
        while open_lst: 
            cheapest_node = None
        #find cheapest node in open_list with lowest estimated distance 
            for node in open_lst:
                if cheapest_node == None or dists[node] + self.heuristic_function(node) < dists[cheapest_node] + self.heuristic_function(cheapest_node):
                    cheapest_node = node 
        #if there is none, then there is no path 
            if cheapest_node == None:
                return None
        #if cheapest_node is the goal_node you have found a path to goal
            if cheapest_node == goal_node:
                reconst_path = []
                while path[cheapest_node] != cheapest_node:
                    reconst_path.append(cheapest_node)
                    cheapest_node = path[cheapest_node]
                reconst_path.append(start_node)
                reconst_path.reverse()
                #return the first node on the path towards goal
                return reconst_path
            
            for node_with_dist in self.grid.get_neighbors_with_dist(cheapest_node[0],cheapest_node[1]):
          # if the current node is not in both open_lst and closed_lst
            # add it to open_lst
                x,y,dist = node_with_dist

                if (x,y) not in open_lst and (x,y) not in closed_lst:
                    open_lst.append((x,y))
                    path[(x,y)] = cheapest_node
                    dists[(x,y)] = dists[cheapest_node] + dist
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
            open_lst.remove(cheapest_node)
            closed_lst.append(cheapest_node)
        return None

environment = Environment.Environment(1, "wasd")
player = Player.Player(environment, "wasd")
enemy = Enemy.Enemy(player)
print(player.grid_pos)
print(enemy.grid_pos)
print(A_Search(enemy))