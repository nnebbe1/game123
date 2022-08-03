# Importieren der Pygame-Bibliothek
from asyncore import write
from lib2to3.pgen2.token import NEWLINE
from pydoc import pipepager
from unicodedata import name
import pygame as pg

import Enemy
import Player
import Environment
import helper
import Platform
import Plots
import random
from helper import *
import time
import csv
from tkinter import *
from tkinter import ttk



def button_click(score, butterflies, pigeons):
    scoreboard_file = open("data\scoreboard.csv", "a", newline="")  
    writer = csv.writer(scoreboard_file)
    user_name_input = str(entry_field.get())
    writer.writerow([str(user_name_input), score, butterflies, pigeons])
    scoreboard_file.close()
    root.destroy()
    return

# initialisieren von pygame
pg.init()

# Fenster öffnen
screen = pg.display.set_mode((WIDTH, HEIGHT))


# Titel für Fensterkopf
pg.display.set_caption(TITEL)
icon = pg.image.load("data\images\dino_right.png")
pg.display.set_icon(icon)


#Game is running as long as is true
gameactive = True

# Bildschirm Aktualisierungen einstellen
clock = pg.time.Clock()

#show start screen
wasd_or_arrow_keys =""
wasd_or_arrow_keys = start_screen(screen)

#create the environment
environment1 = Environment.Environment(1, wasd_or_arrow_keys)




#show start screen
start_screen(screen)

# Schleife Hauptprogramm
while gameactive:
    keys = pg.key.get_pressed()
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameactive = False
            print("Game closed")
        elif event.type == pg.KEYDOWN:

            #W / ARROW UP keys for player, single jump event
            if event.key == pg.K_w and wasd_or_arrow_keys == "wasd":
                environment1.player.jump()
            if event.key == pg.K_UP and wasd_or_arrow_keys == "arrow":
                environment1.player.jump()
            elif event.key == pg.K_SPACE:
                environment1.player_shoot()
        elif event.type == pg.MOUSEBUTTONDOWN:
            print("mousebutton")

    #Game over condition
   # if environment1.player.pos.y > HEIGHT +50:
    #    for sprite in environment1.all_sprites:
    #        sprite.rect.y -= max(environment1.player.vel.y, 10)
    #        if sprite.rect.bottom < 0:
    #            sprite.kill()
    #        if len(environment1.solid_platforms) == 0:
                #end_screen(screen, environment1.score)
                #time.sleep(2)
    #            gameactive = False
                

    # Spielfeld löschen
    screen.fill(LIGHTBLUE)

    # Spielfeld/figuren zeichnen
    environment1.update()

    environment1.all_sprites.draw(screen)

    draw_text_on_screen(screen, str(environment1.score), 20, BLACK, WIDTH * (5 / 6), 15)

    # Fenster aktualisieren
    pg.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

def button_clicked():
    button_click(environment1.get_score(), environment1.get_butterflies(), environment1.get_pigeons())

    
root = Tk()
root.wm_title("Dino's path to victory")
lable = ttk.Label( text="Write your name to put it on the scoreboard!")
lable.pack()
entry_field = Entry(root, width=30)
entry_field.pack()

done_button = ttk.Button(root, text="Done", command=button_clicked)
done_button.pack()
root.mainloop()

pg.quit()

plot1 = Plots.Plot() 
plot1.set_scores()
plot1.plot()



