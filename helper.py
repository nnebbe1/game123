# game settings
from turtle import done
import pygame as pg
import time
import csv
from tkinter import *
from tkinter import ttk

vec = pg.math.Vector2

TITEL = "Dino's path to victory"
WIDTH = 480
HEIGHT = 600
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
PLAYER_JUMP = 9

PLATFORM_LIST1 = [(0,HEIGHT-40, WIDTH,50, "solid"),
                    (WIDTH / 2 - 50, HEIGHT * 5/6, 100, 10, "solid"),
                    (125, HEIGHT * 4 / 6, 100, 10, "solid"),
                    (350, HEIGHT * 3 / 6, 100, 10, "solid"),
                    (175, HEIGHT * 2 / 6, 50, 10, "solid"),
                    (175, HEIGHT * 1 / 6, 50, 10, "solid")]

def draw_text_on_screen(screen, text, size, color, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x ,y)
    screen.blit(text_surface, text_rect)

def start_screen(screen):
    no_key = True
    dino_pos = vec(0, HEIGHT*0.2)
    move_dir = "left"
    while no_key:
        clock = pg.time.Clock()
        clock.tick(40)
        screen.fill(LIGHTBLUE)
        first_platform = pg.Surface((WIDTH, 20))
        first_platform.fill(BROWN)
        screen.blit(first_platform, (0, HEIGHT*0.25))
        draw_text_on_screen(screen, "Move the dino with WASD" , 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.5 )
        draw_text_on_screen(screen,  "Shoot Fireballs with SPACE", 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.6 )
        draw_text_on_screen(screen, "Press ANY key to start", 21, BLACK, WIDTH*0.75, HEIGHT*0.75)

        dino_image = pg.image.load("data\pics\dino_right.png")
        dino_image_rect = dino_image.get_rect()
        screen.blit(dino_image, dino_pos)
       
        if dino_pos.x < WIDTH+1:
            dino_pos.x += 6

        if dino_pos.x > WIDTH-1:
            dino_pos.x = -30

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.KEYUP:
                no_key = False
            if event.type == pg.QUIT:
                pg.quit()

def end_screen(screen, score):
    screen.fill(LIGHTBLUE)
    draw_text_on_screen(screen, "Oh no you died! You're score is {}".format(score) , 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.5 )
    draw_text_on_screen(screen,  "Better Luck next time!", 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.6 )
    pg.display.flip()
    
def user_name_input()->str:
    user_name = ""
    root = Tk()
    lable = ttk.Label( text="Write your name to put it on the scoreboard!")
    lable.pack()
    entry_field = Entry(root, width=30)
    entry_field.pack()
    user_name = entry_field.get()
    done_button = ttk.Button(root, text="Done", command=root.destroy)
    done_button.pack()
    root.mainloop()
    return user_name