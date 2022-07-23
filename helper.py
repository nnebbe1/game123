# game settings
import pygame as pg

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

#player attributes
PLAYER_ACC = 0.4
PLAYER_FRICTION = -0.12
PLAYER_JUMP = 9

PLATFORM_LIST1 = [(0,HEIGHT-40, WIDTH,50),
                    (WIDTH / 2 - 50, HEIGHT * 3/4, 100, 20),
                    (125, HEIGHT -350, 100, 20),
                    (350, 200, 100, 20),
                    (175, 100, 50, 20)]

def draw_text(screen, text, size, color, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x ,y)
    screen.blit(text_surface, text_rect)