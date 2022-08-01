##Hier die Level / Mazes implementieren

from Player import Player
from helper import HEIGHT, PLATFORM_LIST1
import pygame as pg
import Platform
import Player

vec = pg.math.Vector2

class Environment:
    def __init__(self, level) -> None:
        self.level = level
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player.Player(self)
        self.all_sprites.add(self.player)

        if level == 1:
            for plat in PLATFORM_LIST1:
                temp_platform = Platform.Platform(*plat)
<<<<<<< Updated upstream
                self.platforms.add(temp_platform)
=======
                self.solid_platforms.add(temp_platform)
                self.all_platforms.add(temp_platform)
                self.all_sprites.add(temp_platform)
            pigeon = Enemy.Enemy(self.player)
            self.all_sprites.add(pigeon)
            self.enemies.add(pigeon)


    def player_shoot(self):
        temp_fireball = Fireball.Fireball(self.player)
        self.fireballs.add(temp_fireball)
        self.all_sprites.add(temp_fireball)

    def update(self):
        self.all_sprites.update()

        for fireball in self.fireballs:
            hits = pg.sprite.spritecollide(fireball, self.enemies, True)
            if hits:
                pigeon = Enemy.Enemy(self.player)
                self.all_sprites(pigeon)
                self.enemies(pigeon)

        if self.butterflies:
            hits = pg.sprite.spritecollide(self.player, self.butterflies, True)
            if hits:
                self.score += 20
                self.butterfly_score += 1

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
>>>>>>> Stashed changes

    def update(self):
        self.all_sprites.update()

        #check if player hits a platform - only when falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.acc.y = 0