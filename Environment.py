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
import Goal

vec = pg.math.Vector2

# this class implements the game environment and sets it up
# the environment manages all objects in the game (platforms, enemy, player)
# and the interaction betweens these objects
# the environment also manages things like key settings and score
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
        self.grid = Grid.Grid(1)
        self.all_platforms = pg.sprite.Group()
        self.solid_platforms = pg.sprite.Group()
        self.player = Player.Player(self, wasd_or_arrow_keys)
        self.enemy = Enemy.Enemy(self.player)
        self.goal = Goal.Goal()
        self.goals = pg.sprite.Group()
        self.goals.add(self.goal)
        self.all_sprites.add(self.goal)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.enemy)
        self.all_butterflies = pg.sprite.Group()
        self.all_enemies = pg.sprite.Group()
        self.all_enemies.add(self.enemy)
        self.all_fireballs = pg.sprite.Group()
        self.score = 0
        self.butterfly_score = 0
        self.pigeon_score = 0
        
        self.all_sprites.add(self.player)

        #places the platforms in the first level
        self.gamerunning = True
        self.win_or_loose = None

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
        self.all_fireballs.add(temp_fireball)
        self.all_sprites.add(temp_fireball)

    def update(self):
        """
        This function updates all objects in the game
        It also manages interactions between objects (e.g. collisions)
        and the results of these interactions 
        """
        self.all_sprites.update()

        # collision between player and an enemy 
        # if there is a collision the game end by setting the gamerunning var = false
        if self.all_enemies:
            hits = pg.sprite.spritecollide(self.player, self.all_enemies, False)
            if hits:
                self.gamerunning = False
                self.win_or_loose = "loose"    

        # collision between a fireball and an enemy
        # if there is a collision the enemy respawns somewhere else and the pigeon score gets higher
        for fireball in self.all_fireballs: 
            hits = pg.sprite.spritecollide(fireball, self.all_enemies, True)
            if hits:
                hits[0].kill()
                new_enemy = Enemy.Enemy(self.player)
                self.all_sprites.add(new_enemy)
                self.all_enemies.add(new_enemy)
                self.pigeon_score += 1

        #collision between player and a butterfly
        #if collision, picks up butterfly and increase score
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

        #if all buterflies are collected, make the goals flag reachable 
        if len(self.all_butterflies) == 0:
            self.goal.rect.center = vec(WIDTH-95, 35)

        #collision player and goal flag
        #if collision, end game and set win_loose to win
        if self.goals:  
            hits = pg.sprite.spritecollide(self.player, self.goals, False)
            if hits:
                self.gamerunning = False
                self.score += 2000
                self.win_or_loose = "win"
        
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

        
