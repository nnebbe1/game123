import pygame as pg
from helper import *

class Butterfly(pg.sprite.Sprite):
    
    def __init__(self, grid_x, grid_y):
        '''
            Initialises an object of the class Butterfly, which has to be collected by the player
            
            Parameters:
                grid_x(int): It's x-coordinate in the grid
                grid_y(int): It's y-coordinate in the grid
            '''
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('data/images/Butterfly.png')
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self_grid_pos = vec(int(grid_x), int(grid_y))
        self.rect.center = vec((HEIGHT-grid_x*32) +144, (WIDTH-grid_y*32)-160)    
    
      
    
    def update(self):
        pass
        
        
    
        
        
        