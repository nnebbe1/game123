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

vec = pg.math.Vector2

class Environment:
    def __init__(self, level, wasd_or_arrow_keys) -> None:
        self.level = level
        self.wasd_or_arrow_keys = wasd_or_arrow_keys
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.solid_platforms = pg.sprite.Group()
        self.not_solid_platforms = pg.sprite.Group()
        self.player = Player.Player(self, wasd_or_arrow_keys)
        self.all_sprites.add(self.player)

        self.butterflies = pg.sprite.Group()
        self.fireballs = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.score = 0
        self.butterfly_score = 0
        
        self.all_sprites.add(self.player)


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


        

            e = Enemy.Enemy(self.player)
            self.all_sprites.add(e)
            self.enemies.add(e)

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
            
        if self.butterflies:
            hits = pg.sprite.spritecollide(self.player, self.butterflies, True)
            if hits:
                self.score += 20
                self.butterfly_score += 1
            

        #check if player hits a platform - only when falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.solid_platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.not_solid_platforms, True)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = -9
        
        # if player reaches top of screen, move "screen"
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.all_platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10
            for b in self.butterflies:
                b.rect.y += abs(self.player.vel.y)
                if b.rect.top >= HEIGHT:
                    b.kill()
                    

        #spawn new platforms if old ones get deleted
        while len(self.solid_platforms) < 6:
            random_nr = random.randrange(1, 10)
            if random_nr > 2:
                solidity_state = "solid"
                width = random.randrange(50, 100)
                p = Platform.Platform(random.randrange(0, WIDTH-width),
                                    -10,width, 10, solidity_state)
            elif random_nr <= 2:
                solidity_state = "not_solid"
                width = random.randrange(50, 100)
                p = Platform.Platform(random.randrange(0, WIDTH-width),
                                    -30,width, 10, solidity_state)

            
            if solidity_state == "solid":
                self.solid_platforms.add(p)
            else:
                self.not_solid_platforms.add(p)
            self.all_platforms.add(p)
            self.all_sprites.add(p)
            
        while len(self.butterflies) < random.randrange(5):
            b = Butterfly.Butterfly(random.randrange(0, self.player.rect.top), random.randrange(0, WIDTH))
            self.all_sprites.add(b)
            self.butterflies.add(b)
                                    

    def get_pos(self):
        return self.player.get_pos()
        
