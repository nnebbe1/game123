##Hier die Level / Mazes implementieren


from Player import Player
from helper import *
import pygame as pg
import Platform
import Player
import Fireball
import random
import Butterfly
import Enemy
import Grid

vec = pg.math.Vector2

class Environment:
    def __init__(self, level, wasd_or_arrow_keys):
        '''
            Initialises an object of the class Environment

            Parameters:
                level(int): the level of the game
                wasd_or_arrow_keys(str): determines whether player is moved by wasd or the arrow keys
        '''
        self.level = level
        self.wasd_or_arrow_keys = wasd_or_arrow_keys
        self.all_sprites = pg.sprite.Group()
        self.grid = Grid.Grid(level)
        self.all_platforms = pg.sprite.Group()
        self.solid_platforms = pg.sprite.Group()
        self.not_solid_platforms = pg.sprite.Group()
        self.player = Player.Player(self, wasd_or_arrow_keys)
        self.all_sprites.add(self.player)
        self.all_butterflies = pg.sprite.Group()
        self.fireballs = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.score = 0
        self.butterfly_score = 0
        self.pigeon_score = 0
        
        self.all_sprites.add(self.player)

        #places the platforms in the first level
        if level == 1:
            print(self.grid.grid)
            for x in range(30):
                for y in range(25):
                    if self.grid.grid[x][y] == 1:
                        temp_platform = Platform.Platform(x,y, "solid")
                        self.all_platforms.add(temp_platform)
                        self.solid_platforms.add(temp_platform)
                        self.all_sprites.add(temp_platform)
            
            for x in range(30):
                for y in range(25):
                    if self.grid.grid[x][y] == 2:
                        temp_butterfly= Butterfly.Butterfly(x,y)
                        self.all_butterflies.add(temp_butterfly)
                        self.all_sprites.add(temp_butterfly)

    #the player can shoot fireballs to shoot the enemy
    def player_shoot(self):
        temp_fireball = Fireball.Fireball(self.player)
        self.fireballs.add(temp_fireball)
        self.all_sprites.add(temp_fireball)

    def update(self):
        '''
            Updates the Environment by updating all Sprites and checking for collisions

            Returns:
                Boolean -> determines whether or not game is over
        '''
        self.all_sprites.update()
    
        #checks whether any fireballs have hit the enemy - which is then eliminated
        #the pigeon score increases for every enemy that is eliminated
        for fireball in self.fireballs: 
            hits = pg.sprite.spritecollide(fireball, self.enemies, True)
            if hits:
                e = Enemy.Enemy(self.player)
                self.all_sprites.add(e)
                self.enemies.add(e)
                self.pigeon_score += 1

        #the player collects the butterflies
        #this increases the overall score and the butterfly score
        if self.all_butterflies:
            hits = pg.sprite.spritecollide(self.player, self.all_butterflies, True)
            if hits:
                self.score += 20
                self.butterfly_score += 1

        #if the enemy hits the player the game is over    
        if self.enemies:
            hits = pg.sprite.spritecollide(self.player, self.enemies, True)
            if hits:
                return False
            
        #check if player hits a platform - only when falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.solid_platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        if self.player.vel.y < 0:
            hits = pg.sprite.spritecollide(self.player, self.solid_platforms, False)
            if hits:
                self.player.pos.y += 4
                self.player.vel.y = 0
        
                                    

    def get_pos(self):
        '''
            Returns:
                position of the player
        '''
        return self.player.get_pos()

    def get_score(self):
        '''
            Returns:
                self.score(int): the player's score
        '''
        return self.score

    def get_butterflies(self):
        '''
            Returns:
                self.butterfly_score(int): the player's butterfly score
        '''
        return self.butterfly_score

    def get_pigeons(self):
        '''
            Returns:
                self.pigeon_score(int): the player's pigeon score
        '''
        return self.pigeon_score

        
