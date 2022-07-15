##Hier die Level / Mazes implementieren

import pygame
import Brick

class Environment:
    def __init__(self, level) -> None:
        self.bricks = list()
        self.level = level
        if level == 1:
            for i in range(10):
                self.bricks.append(Brick.Brick(64*i,64))


