# Importieren der Pygame-Bibliothek
import pygame
import Agent
import Player
import Environment
import helper
import Brick
# initialisieren von pygame
pygame.init()

# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

# Fenster öffnen
screen = pygame.display.set_mode((640, 640))

# Titel für Fensterkopf
pygame.display.set_caption("Maze Runners 2000 by Emily and Norman")
icon = pygame.image.load("data\pics\dino_right.png")
pygame.display.set_icon(icon)

# solange die Variable True ist, soll das Spiel laufen
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
    #A and D keys for player, continuous walking
    if keys[pygame.K_a]:
        player1.walk_left()
        player1.icon = pygame.image.load("data\pics\dino_left.png")  
    if keys[pygame.K_d]:
        player1.walk_right()
        player1.icon = pygame.image.load("data\pics\dino_right.png")  

    # Spiellogik hier integrieren

    # Spielfeld löschen
    screen.fill(WEISS)

    # Spielfeld/figuren zeichnen
    screen.blit(player1.icon, (player1.xPos, player1.yPos))
    for brick in environment1.bricks:
        screen.blit(brick.icon, (brick.xPos, brick.yPos))
    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()