# Importieren der Pygame-Bibliothek
import pygame
import Agent
import Player
import Environment
import helper
import Platform
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
                environment1.player.jump()
            elif event.key == pygame.K_s:
                None
                #environment1.player.fall()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("mousebutton")

    # Spielfeld löschen
    screen.fill(WHITE)

    # Spielfeld/figuren zeichnen
    environment1.update()
    screen.blit(environment1.player.icon, environment1.player.rect.midbottom)
    for platform in environment1.platforms:
        screen.blit(platform.image, (platform.rect.x, platform.rect.y+30))
    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()