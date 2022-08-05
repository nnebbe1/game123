# game settings


import pygame as pg
import time
import csv
from tkinter import *
from tkinter import ttk

vec = pg.math.Vector2

TITEL = "Dino's path to victory"
WIDTH = 960
HEIGHT = 800
FPS = 60
FONT_NAME = 'arial'
font_name = pg.font.match_font(FONT_NAME)

ORANGE  = ( 255, 140, 0)
RED     = ( 255, 0, 0)
GREEN   = ( 0, 255, 0)
BLACK   = ( 0, 0, 0)
WHITE   = ( 255, 255, 255)
BROWN   = ( 200, 100, 100)
LIGHTBLUE = (0, 220, 220)

#player attributes
PLAYER_ACC = 0.4
PLAYER_FRICTION = -0.12
PLAYER_JUMP = 6
PLAYER_NAME = ""

#PLATFORM_LIST1 = [(0,HEIGHT-40, WIDTH,50, "solid"),
                   # (WIDTH / 2 - 50, HEIGHT * 5/6, 100, 40, "solid"),
                    #(125, HEIGHT * 4 / 6, 100, 40, "solid"),
                    #(350, HEIGHT * 3 / 6, 100, 40, "solid"),
                    #(175, HEIGHT * 2 / 6, 50, 40, "solid"),
                    #(175, HEIGHT * 1 / 6, 50, 40, "solid")]

def draw_text_on_screen(screen, text, size, color, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x ,y)
    screen.blit(text_surface, text_rect)

def A_Search(self)->tuple:
        # get start and goal from the position of the pigeon and the positon of the player
        start_node = (self.grid_pos.x, self.grid_pos.y)
        goal_node = (self.player.grid_pos.x, self.player.grid_pos.y-1)

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
                try:
                    return reconst_path[1]
                except:
                    return reconst_path[0]
            
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
    

def start_screen(screen)->str:
    no_key = True
    dino_pos = vec(0, HEIGHT*0.2)
    move_dir = "left"
    wasd_or_arrow_keys = ""
    while no_key:
        clock = pg.time.Clock()
        clock.tick(40)
        screen.fill(LIGHTBLUE)
        first_platform = pg.Surface((WIDTH, 20))
        first_platform.fill(BROWN)
        screen.blit(first_platform, (0, HEIGHT*0.25))
        draw_text_on_screen(screen, "Move the dino with WASD or ARROW Keys" , 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.5 )
        draw_text_on_screen(screen,  "Shoot Fireballs with SPACE", 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.6 )
        draw_text_on_screen(screen, "Press W or ARROW UP to choose control schema", 21, BLACK, WIDTH*0.75, HEIGHT*0.75)

        dino_image = pg.image.load("data\images\dino_right.png")
        dino_image_rect = dino_image.get_rect()
        screen.blit(dino_image, dino_pos)
       
        if dino_pos.x < WIDTH+1:
            dino_pos.x += 6

        if dino_pos.x > WIDTH-1:
            dino_pos.x = -30

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    wasd_or_arrow_keys = "wasd"
                    no_key = False 
                    print("WASD Control")
                if event.key == pg.K_UP:
                    wasd_or_arrow_keys = "arrow"
                    no_key = False
                    print("Arrow Control")
                if event.type == pg.QUIT:
                    print("QUIT")
                    pg.quit()
                    #return None
    return wasd_or_arrow_keys

def end_screen(screen, win_or_loose, score):
    if win_or_loose == "loose":
        screen.fill(LIGHTBLUE)
        draw_text_on_screen(screen, "Oh no you died! You're score is {}".format(score) , 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.5 )
        draw_text_on_screen(screen,  "Better Luck next time!", 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.6 )
        pg.display.flip()

    if win_or_loose == "win":
        screen.fill(LIGHTBLUE)
        draw_text_on_screen(screen, "You made it! You're score is {}".format(score) , 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.5 )
        draw_text_on_screen(screen,  "GREAT JOB!", 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.6 )
        pg.display.flip()

def button_click(root, entry_field):
    PLAYER_NAME = entry_field.get()
    print(PLAYER_NAME)
    root.destroy()
    
def user_name_input()->str:
    root = Tk()
    lable = ttk.Label( text="Write your name to put it on the scoreboard!")
    lable.pack()
    entry_field = Entry(root, width=30)
    entry_field.pack()
    user_name = entry_field.get()
    done_button = ttk.Button(root, text="Done", command=button_click(root, entry_field))
    done_button.pack()
    root.mainloop()

    return user_name
