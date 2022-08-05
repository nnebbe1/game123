
import pygame as pg
from tkinter import *
from tkinter import ttk
vec = pg.math.Vector2

"""
This class implemets a lot of different helper variables and functions that are used in the project

"""

# global variables
TITEL = "Dino's path to victory"
WIDTH = 960
HEIGHT = 800
FPS = 60
FONT_NAME = 'arial'
font_name = pg.font.match_font(FONT_NAME)

ORANGE  = ( 255, 140, 0)
RED     = ( 255, 0, 0)
GREEN   = ( 0, 255, 0)
BLACK   = ( 0, 0, 0)
WHITE   = ( 255, 255, 255)
BROWN   = ( 200, 100, 100)
LIGHTBLUE = (0, 220, 220)

#player attributes
PLAYER_ACC = 0.4
PLAYER_FRICTION = -0.12
PLAYER_JUMP = 6
PLAYER_NAME = ""

def draw_text_on_screen(screen, text, size, color, x, y):
    '''
        Draws text on the screen

        Parameters:
            screen: which screen to draw on
            text(str): the text to be drawn
            size(int): font size
            color(str): font color
            x(int), y(int): coordinates of the text on the screen
    
    '''
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x ,y)
    screen.blit(text_surface, text_rect)

def A_Search(self)->tuple:
        """
        This function implements the A Star search algorithm.
        It searches for the shortest path between the grid position of the Enemy (pigeon)
        and the grid position of the player char.
        Once a path has been found, it returns the next grid node that the enemy has to go to
        to reach the player


        Parameters:
                self(Enemy obj): an instance of the Enemy class         

        Returns:

            reconst_path[1](tupel): a tupel of grid coordiations of the next grid node that the enemy has to go to
                OR
            reconst_path[0](tupel): a tupel of grid coordiations of the next grid node that the enemy has to go to

        

        """
        # get start and goal from the position of the pigeon and the positon of the player
        start_node = (self.grid_pos.x, self.grid_pos.y)
        goal_node = (self.player.grid_pos.x, self.player.grid_pos.y-1)

        #open list and closed list
        open_lst = list()
        open_lst.append(start_node)
        closed_lst = list()

        #dict with the distances of the different nodes
        dists = {}
        dists[start_node] = 0

        #dict for the found path
        path = {}
        path[start_node] = start_node
    
        while open_lst: 
            cheapest_node = None
        #find cheapest node in open_list with lowest estimated distance 
            for node in open_lst:
                if cheapest_node == None or dists[node] + self.heuristic_function(node) < dists[cheapest_node] + self.heuristic_function(cheapest_node):
                    cheapest_node = node 
        #if there is none, then there is no path 
            if cheapest_node == None:
                return None
        #if cheapest_node is the goal_node you have found a path to goal
        #if so, reconstruct it
            if cheapest_node == goal_node:
                reconst_path = []
                while path[cheapest_node] != cheapest_node:
                    reconst_path.append(cheapest_node)
                    cheapest_node = path[cheapest_node]
                reconst_path.append(start_node)
                reconst_path.reverse()
                #return the first node on the path towards goal if possible
                try:
                    return reconst_path[1]
                except:
                    return reconst_path[0]


            # get the neighbouring nodes of the node that i currently investigated
            for node_with_dist in self.grid.get_neighbors_with_dist(cheapest_node[0],cheapest_node[1]):
          
                x,y,dist = node_with_dist
                # if the current node is not in  open_lst or closed_lst
                # add it to open_lst

                if (x,y) not in open_lst and (x,y) not in closed_lst:
                    open_lst.append((x,y))
                    path[(x,y)] = cheapest_node
                    dists[(x,y)] = dists[cheapest_node] + dist

            # once all neighbours have been added to the openlist, remove the current node
            open_lst.remove(cheapest_node)
            closed_lst.append(cheapest_node)

        # if it reaches here, no path has been found
        return None
    

def start_screen(screen)->str:
    '''
        Defines the start screen
        It shows some basic game instruction
        Also it waits for a user input, either W or ARROW UP and returns an according string
        This will determine the control schema of the current game session

        Parameters:
            screen(Pygame.display): The screen on which the game content is drawn

        Returns:
            wasd_or_arrow_keys(str): determines whether player is controlled with wasd or arrow keys
    '''
    no_key = True
    dino_pos = vec(0, HEIGHT*0.2)
    wasd_or_arrow_keys = ""

    # mainloop waiting for user input
    while no_key:
        clock = pg.time.Clock()
        clock.tick(40)
        #draw basic platform, basic dino image and text labels
        screen.fill(LIGHTBLUE)
        first_platform = pg.Surface((WIDTH, 20))
        first_platform.fill(BROWN)
        screen.blit(first_platform, (0, HEIGHT*0.25))
        draw_text_on_screen(screen, "Move the dino with WASD or ARROW Keys" , 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.5 )
        draw_text_on_screen(screen,  "Shoot Fireballs with SPACE", 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.6 )
        draw_text_on_screen(screen, "Press W or ARROW UP to choose control schema", 21, BLACK, WIDTH*0.75, HEIGHT*0.75)

        dino_image = pg.image.load("data\images\dino_right.png")

        #draw dino image
        screen.blit(dino_image, dino_pos)
       
       #make dino wrap around scren
        if dino_pos.x < WIDTH+1:
            dino_pos.x += 6

        if dino_pos.x > WIDTH-1:
            dino_pos.x = -30

        pg.display.flip()

        #checks which keys user wants to use 
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    wasd_or_arrow_keys = "wasd"
                    no_key = False 
                    print("WASD Control")
                if event.key == pg.K_UP:
                    wasd_or_arrow_keys = "arrow"
                    no_key = False
                    print("Arrow Control")
                if event.type == pg.QUIT:
                    print("QUIT")
                    pg.quit()

    return wasd_or_arrow_keys

def end_screen(screen, win_or_loose, score):
    '''
        Defines the game over screen

        Parameter:
            screen(pygame.display): The screen on which the game content is drawn
            win_or_loose(str): A string containing "win" or "loose", determines the end screen
            score(int): The score that the player achieved
    '''

    # if game lost - caught by pigeon
    if win_or_loose == "loose":
        screen.fill(LIGHTBLUE)
        draw_text_on_screen(screen, "Oh no you died! You're score is {}".format(score) , 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.5 )
        draw_text_on_screen(screen,  "Better Luck next time!", 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.6 )
        pg.display.flip()

    #if game won - collected all butterflies and reached goal flag
    if win_or_loose == "win":
        screen.fill(LIGHTBLUE)
        draw_text_on_screen(screen, "You made it! You're score is {}".format(score) , 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.5 )
        draw_text_on_screen(screen,  "GREAT JOB!", 21, BLACK, WIDTH * 0.5 , HEIGHT * 0.6 )
        pg.display.flip()


def button_click(root, entry_field):
    """
    This function determines what happens when the user clicks the done button on the
    name input dialog
    
    Parameter :
        root(tkinter obj): the base of the input form
        entry_field(tking obj): the entry field in which the user puts his name
    """
    PLAYER_NAME = entry_field.get()
    print(PLAYER_NAME)
    root.destroy()
    
def user_name_input()->str:

    """
    Opens a user dialog windown in which the user is prompted to put in his name.
    This is used to later write the name and score into the scoreboard.csv
    This makes use of the tkinter package

    Returns:
        user_name(str): The str that the user put in
    """


    root = Tk()
    lable = ttk.Label( text="Write your name to put it on the scoreboard!")
    lable.pack()
    entry_field = Entry(root, width=30)
    entry_field.pack()
    user_name = entry_field.get()
    done_button = ttk.Button(root, text="Done", command=button_click(root, entry_field))
    done_button.pack()
    root.mainloop()

    return user_name
