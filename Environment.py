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

# this class implements the game environment and sets it up
# the environment manages all objects in the game (platforms, enemy, player)
# and the interaction betweens these objects
# the environment also manages things like key settings and score
class Environment:
    def __init__(self, level, wasd_or_arrow_keys) -> None:
        self.level = level
        self.wasd_or_arrow_keys = wasd_or_arrow_keys
        self.all_sprites = pg.sprite.Group()
        self.grid = Grid.Grid(1)
        self.all_platforms = pg.sprite.Group()
        self.solid_platforms = pg.sprite.Group()
        self.player = Player.Player(self, wasd_or_arrow_keys)
        self.enemy = Enemy.Enemy(self.player)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.enemy)
        self.all_butterflies = pg.sprite.Group()
        self.fireballs = pg.sprite.Group()
        self.score = 0
        self.butterfly_score = 0

        #leaves the possibility for the implementation / additon of more levels with different setup
        if level == 1:
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


    def player_shoot(self):
        """
        This function adds a fireball object
        """
        temp_fireball = Fireball.Fireball(self.player)
        self.fireballs.add(temp_fireball)
        self.all_sprites.add(temp_fireball)

    def update(self):
        """
        This function updates all objects in the game
        It also manages interactions between objects (e.g. collisions)
        and the results of these interactions 
        """
        self.all_sprites.update()

        # collision between a fireball and an enemy
        for fireball in self.fireballs: 
            hits = pg.sprite.spritecollide(fireball, self.enemies, True)
            if hits:
                e = Enemy.Enemy(self.player)
                self.all_sprites.add(e)
                self.enemies.add(e)

        #collision between player and a butterfly
        if self.all_butterflies:
            hits = pg.sprite.spritecollide(self.player, self.all_butterflies, True)
            if hits:
                self.score += 20
                self.butterfly_score += 1
            
        #check if player hits a platform when falling, if yes, stop movement
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.solid_platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        #check if player hits a platform when jumping, if yes, stop movement
        if self.player.vel.y < 0:
            hits = pg.sprite.spritecollide(self.player, self.solid_platforms, False)
            if hits:
                self.player.pos.y += 4
                self.player.vel.y = 0
                                    
    def get_pos(self):
        return self.player.get_pos()
        
