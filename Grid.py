import pygame as pg 
import math


class Grid:
    

    def  __init__(self, level):
        '''
            Initialises the Grid in which the environment is divided

            Parameters:
                level(int): determines the level of the game and thereby the outlay of the grid
        '''

        self.grid =  [[0 for j in range(25)] for i in range(30)] 


        #Defines the ground as a Platform (coded with 1)
        for i in range(30):
            self.grid[i][1] = 1

        if level == 1:
            # Define all grid cells which will have a platform. Platforms are coded with 1
            for i in range(7,9):
                self.grid[i][2] = 1

            for i in range(15,20):
                self.grid[i][3] = 1

            for i in range(6):
                self.grid[i][4] = 1

            for i in range(19,27):
                self.grid[i][6] = 1

            for i in range(5,11):
                self.grid[i][7] = 1

            for i in range(11,19):
                self.grid[i][10] = 1

            for i in range(26,30):
                self.grid[i][10] = 1

            for i in range(4,10):
                self.grid[i][13] = 1

            for i in range(28,30):
                self.grid[i][13] = 1

            for i in range(19,24):
                self.grid[i][14] = 1

            for i in range(5):
                self.grid[i][16] = 1

            for i in range(11,17):
                self.grid[i][16] = 1

            for i in range(5,11):
                self.grid[i][19] = 1

            for i in range(18,24):
                self.grid[i][19] = 1

            for i in range(10,13):
                self.grid[i][22] = 1

            for i in range(26,29):
                self.grid[i][23] = 1

            for i in range(7):
                self.grid[i][23] = 1

            # Define all grid cells which will have a butterfly. Butterflies are coded with 2
            
            self.grid[8][3] = 2
            self.grid[16][4] = 2
            self.grid[19][4] = 2

            self.grid[1][5] = 2
            self.grid[3][5] = 2
            self.grid[5][5] = 2

            self.grid[20][7] = 2
            self.grid[23][7] = 2
            self.grid[26][7] = 2

            self.grid[6][8] = 2
            self.grid[8][8] = 2
            self.grid[10][8] = 2


            self.grid[13][11] = 2
            self.grid[15][11] = 2
            self.grid[17][11] = 2

            self.grid[27][11] = 2
            self.grid[29][11] = 2

            for i in range(4,10):
                self.grid[5][14] = 2
                self.grid[9][14] = 2

            for i in range(28,30):
                self.grid[i][14] = 2

            for i in range(19,24):
                self.grid[i][15] = 2

            for i in range(5):
                self.grid[i][17] = 2

            for i in range(11,17):
                self.grid[i][17] = 2

            for i in range(5,11):
                self.grid[i][20] = 2

            for i in range(18,24):
                self.grid[i][20] = 2

            for i in range(10,13):
                self.grid[i][23] = 2

            for i in range(26,29):
                self.grid[i][24] = 2

            for i in range(7):
                self.grid[i][24] = 2

        if level == 2:

            for i in range(6):
                self.grid[i][3] = 1

            for i in range(11,17):
                self.grid[i][3] = 1

            for i in range(25,30):
                self.grid[i][3] = 1

            for i in range(21,24):
                self.grid[i][5] = 1
                 
            for i in range(25,30):
                self.grid[i][8] = 1

            for i in range(2,8):
                self.grid[i][9] = 1

            for i in range(27,30):
                self.grid[i][11] = 1

            for i in range(2,5):
                self.grid[i][12] = 1

            for i in range(11,17):
                self.grid[i][12] = 1

            for i in range(6,11):
                self.grid[i][15] = 1

            for i in range(22,26):
                self.grid[i][16] = 1

            for i in range(2,6):
                self.grid[i][18] = 1

            for i in range(14,20):
                self.grid[i][18] = 1

            for i in range(6,13):
                self.grid[i][21] = 1

            for i in range(1,5):
                self.grid[i][23] = 1
                



