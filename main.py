# Importieren der Pygame-Bibliothek
import pygame
import Agent
import Player
import Environment
import helper
import Brick
import random
from helper import *


# initialisieren von pygame
pygame.init()

# Fenster öffnen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Titel für Fensterkopf
pygame.display.set_caption(TITEL)
icon = pygame.image.load("data\pics\dino_right.png")
pygame.display.set_icon(icon)

#Game is running as long as is true
gameactive = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

#create the player char
player1 = Player.Player()

#create the environment
environment1 = Environment.Environment(1)

# Schleife Hauptprogramm
while gameactive:
    keys = pygame.key.get_pressed()
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameactive = False
            print("Game closed")
        elif event.type == pygame.KEYDOWN:

            #W and S keys for player, single jump event
            if event.key == pygame.K_w:
                player1.jump()
            elif event.key == pygame.K_s:
                player1.fall()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("mousebutton")

    # Spielfeld löschen
    screen.fill(WHITE)

    # Spielfeld/figuren zeichnen
    player1.update()
    screen.blit(player1.icon, player1.pos)
    for brick in environment1.bricks:
        screen.blit(brick.icon, (brick.xPos, brick.yPos))
    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()