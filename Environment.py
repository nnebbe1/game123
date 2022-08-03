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
    def __init__(self, level, wasd_or_arrow_keys) -> None:
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


    def player_shoot(self):
        temp_fireball = Fireball.Fireball(self.player)
        self.fireballs.add(temp_fireball)
        self.all_sprites.add(temp_fireball)

    def player_shoot(self):
        temp_fireball = Fireball.Fireball(self.player)
        self.fireballs.add(temp_fireball)
        self.all_sprites.add(temp_fireball)

    def update(self):
        self.all_sprites.update()
        for fireball in self.fireballs: 
            hits = pg.sprite.spritecollide(fireball, self.enemies, True)
            if hits:
                e = Enemy.Enemy(self.player)
                self.all_sprites.add(e)
                self.enemies.add(e)
                self.pigeon_score += 1

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
        
        # if player reaches top of screen, move "screen"
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.all_platforms:
                plat.rect.y += abs(self.player.vel.y)
            for butterfly in self.all_butterflies:
                butterfly.rect.y += abs(self.player.vel.y)
            for enemy in self.enemies:
                enemy.rect.y += abs(self.player.vel.y)

        if self.player.rect.top >= HEIGHT * 3/ 4:
            self.player.pos.y -= abs(self.player.vel.y)
            for plat in self.all_platforms:
                plat.rect.y -= abs(self.player.vel.y)
            for butterfly in self.all_butterflies:
                butterfly.rect.y -= abs(self.player.vel.y)
            for enemy in self.enemies:
                enemy.rect.y -= abs(self.player.vel.y)
            
            for b in self.all_butterflies:
                b.rect.y += abs(self.player.vel.y)
                if b.rect.top >= HEIGHT:
                    b.kill()
            
        while len(self.all_butterflies) < random.randrange(5):
            b = Butterfly.Butterfly(random.randrange(0, self.player.rect.top), random.randrange(0, WIDTH))
            self.all_sprites.add(b)
            self.all_butterflies.add(b)
                                    

    def get_pos(self):
        return self.player.get_pos()

    def get_score(self):
        return self.score

    def get_butterflies(self):
        return self.butterfly_score

    def get_pigeons(self):
        return self.pigeon_score

        
