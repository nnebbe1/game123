# game settings

import pygame as pg
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

def draw_text_on_screen(screen, text, size, color, x, y):
    '''
        Draws text on the screen

        Parameters:
            screen: which screen to draw on
            text(str): the text to be drawn
            size(int): font size
            color(str): font color
            x(int), y(int): coordinates of the text on the screen
    
    '''
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x ,y)
    screen.blit(text_surface, text_rect)

def start_screen(screen):
    '''
        Defines the start screen

        Returns:
            wasd_or_arrow_keys(str): determines whether player is controlled with wasd or arrow keys
    '''
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

        #checks which keys user wants to use 
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

    return wasd_or_arrow_keys

def end_screen(screen, score):
    '''
        Defines the game over screen
    '''
    screen.fill(LIGHTBLUE)
    draw_text_on_screen(screen, "Oh no you died! You're score is {}".format(score) , 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.5 )
    draw_text_on_screen(screen,  "Better Luck next time!", 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.6 )
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
