##Hier die Level / Mazes implementieren


from Player import Player
from helper import HEIGHT, PLATFORM_LIST1
import pygame as pg
import Platform
import Player
import Fireball

vec = pg.math.Vector2

class Environment:
    def __init__(self, level) -> None:
        self.level = level
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.fireballs = pg.sprite.Group()
        self.player = Player.Player(self)
        self.all_sprites.add(self.player)

        if level == 1:
            for plat in PLATFORM_LIST1:
                temp_platform = Platform.Platform(*plat)
                self.platforms.add(temp_platform)
                self.all_sprites.add(temp_platform)

    def player_shoot(self):
        temp_fireball = Fireball.Fireball(self.player)
        self.fireballs.add(temp_fireball)
        self.all_sprites.add(temp_fireball)

    def update(self):
        self.all_sprites.update()

        #check if player hits a platform - only when falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0