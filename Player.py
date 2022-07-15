import pygame

class Player:
    def __init__(self) -> None:
        self.xPos = 0
        self.yPos = 0
        self.icon = pygame.image.load("data\pics\dino_right.png")
        self.player_rect = self.icon.get_rect()

    def jump(self):
        self.yPos = self.yPos - 20
    def fall(self):
        self.yPos = self.yPos + 20
    def walk_left(self):
        self.xPos = self.xPos - 10
    def walk_right(self):
        self.xPos = self.xPos + 10