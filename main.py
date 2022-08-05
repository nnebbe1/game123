
# Importieren der Pygame-Bibliothek
"""
from asyncore import write
from lib2to3.pgen2.token import NEWLINE
from pydoc import pipepager
from unicodedata import name
"""
import pygame as pg


import Environment
import Plots
from helper import *
import csv
from tkinter import *
from tkinter import ttk



def button_click(score, butterflies, pigeons):
    '''
        Saves the user data in a csv

        Parameters:
            score(int): the user's score
            butterflies(int): the user's butterfly score
            pigeons(int); the user's pigeon score
    '''
    scoreboard_file = open("data\scoreboard.csv", "a", newline="")  
    writer = csv.writer(scoreboard_file)
    user_name_input = str(entry_field.get())
    writer.writerow([str(user_name_input), score, butterflies, pigeons])
    scoreboard_file.close()
    root.destroy()
    return

#initialising pygame
pg.init()

# opening window
screen = pg.display.set_mode((WIDTH, HEIGHT))


# setting game icon and title
pg.display.set_caption(TITEL)
icon = pg.image.load("data\images\dino_right.png")
pg.display.set_icon(icon)


#Game is running as long as is true
gameactive = True

# clock for updating the screen
clock = pg.time.Clock()

#show start screen
wasd_or_arrow_keys =""
wasd_or_arrow_keys = start_screen(screen)

#create the environment
environment1 = Environment.Environment(1, wasd_or_arrow_keys)


# main game lopp
while environment1.gamerunning:

    keys = pg.key.get_pressed()
    # checks whether user has pressed a button 
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

    # deleting the playing field
    screen.fill(LIGHTBLUE)

    # drawing the environment
    environment1.update()

    environment1.all_sprites.draw(screen)
    #Makes sure that the enemy is always at top layer of screen and can always be seen
    environment1.all_enemies.draw(screen)
    #Shows the current score
    draw_text_on_screen(screen, str(environment1.score), 20, BLACK, WIDTH * (5 / 6), 15)

    # updating screen
    pg.display.flip()

    # refresh-time
    clock.tick(60)


def button_clicked():
    '''
        A function to use the button click within tkinter
    '''
    button_click(environment1.get_score(), environment1.get_butterflies(), environment1.get_pigeons())

    
#show endscreen
end_screen(screen, environment1.win_or_loose, environment1.score)

# User Interface for Name input    

root = Tk()
root.wm_title("Dino's path to victory")
lable = ttk.Label( text="Write your name to put it on the scoreboard!")
lable.pack()
entry_field = Entry(root, width=30)
entry_field.pack()

done_button = ttk.Button(root, text="Done", command=button_clicked)
done_button.pack()
root.mainloop()

#exiting pygame
pg.quit()

#creating plot for user's scores
plot1 = Plots.Plot() 
plot1.set_scores()
plot1.plot()



