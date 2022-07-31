##Hier die Level / Mazes implementieren


from Player import Player
from helper import *
import pygame as pg
import Platform
import Player
import Fireball
import random

vec = pg.math.Vector2

class Environment:
    def __init__(self, level) -> None:
        self.level = level
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.solid_platforms = pg.sprite.Group()
        self.not_solid_platforms = pg.sprite.Group()
        self.fireballs = pg.sprite.Group()
        self.player = Player.Player(self)
        self.all_sprites.add(self.player)
        self.score = 0

        if level == 1:
            for plat in PLATFORM_LIST1:
                temp_platform = Platform.Platform(*plat)
                self.solid_platforms.add(temp_platform)
                self.all_platforms.add(temp_platform)
                self.all_sprites.add(temp_platform)

    def player_shoot(self):
        temp_fireball = Fireball.Fireball(self.player)
        self.fireballs.add(temp_fireball)
        self.all_sprites.add(temp_fireball)

    def update(self):
        self.all_sprites.update()

        #check if player hits a platform - only when falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.solid_platforms, False)
            # check the 4 possible collisions
            if hits:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
         
                

        if self.player.vel.y < 0:
            hits = pg.sprite.spritecollide(self.player, self.solid_platforms, False)
            if hits:
                self.player.pos.y += 3
                self.player.vel.y = 0



    #   if self.player.vel.y > 0:
    #      hits = pg.sprite.spritecollide(self.player, self.not_solid_platforms, True)
      #      if hits:
       #         self.player.pos.y = hits[0].rect.top
       #         self.player.vel.y = -9
        
        # if player reaches top of screen, move "screen"
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.all_platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()


        


