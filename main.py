# Importieren der Pygame-Bibliothek
import pygame
from prompt_toolkit import prompt

import Agent
import Player
import Environment
import helper
import Platform
import random
from helper import *
import time
import csv
from tkinter import *
from tkinter import ttk





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

#show start screen
start_screen(screen)

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
            elif event.key == pygame.K_SPACE:
                environment1.player_shoot()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("mousebutton")

    #Game over condition
    if environment1.player.pos.y > HEIGHT +50:
        for sprite in environment1.all_sprites:
            sprite.rect.y -= max(environment1.player.vel.y, 10)
            if sprite.rect.bottom < 0:
                sprite.kill()
            if len(environment1.solid_platforms) == 0:
                end_screen(screen, environment1.score)
                time.sleep(2)
                gameactive = False
                
                

    # Spielfeld löschen
    screen.fill(LIGHTBLUE)

    # Spielfeld/figuren zeichnen
    environment1.update()

    environment1.all_sprites.draw(screen)

    draw_text_on_screen(screen, str(environment1.score), 20, BLACK, WIDTH * (5 / 6), 15)

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

# open csv file and write name
with open("data\scoreboard.csv", "a") as csv_file:
    writer = csv.writer(csv_file)

user_name_input()    

pygame.quit()

