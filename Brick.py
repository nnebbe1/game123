import pygame

class Brick:
    def __init__(self, xPos, yPos) ->None:
        self.xPos = xPos
        self.yPos = yPos
        self.icon = pygame.image.load("data\pics\Brick.png")
        self.brick_rect = self.icon.get_rect()