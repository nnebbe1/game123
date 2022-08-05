"""

Unfortunately this class has to be commented out, because of the compatibility issues between packages


from matplotlib import pyplot as plt
import pandas as pd
from helper import *

#Plot class for creating a Plot at the end of the game that displays scores
class Plot():
    
    def __init__(self):
        '''
            Initialises a Plot object
        '''
        self.x = [10, 15]
        self.x2 = [10.7, 15.7]
        self.score = 0
        self.bflies = 0
        self.pigeons = 0
        self.highsc = 0
        self.highb = 0
        self.highp = 0
        self.name = ''
        self.last_row = []
        self.color = RED
        self.tick_label = ["Butterflies", "Pigeons"]
        self.scoreboard = pd.read_csv('data\scoreboard.csv')
        self.fig, self.axes = plt.subplots(nrows = 2, ncols = 1)

   
    def set_scores(self):
        '''
            Sets the different scores to the correct numbers from the csv file  
        '''
        self.last_row = self.scoreboard.iloc[-1].tolist()
        self.name = self.last_row[0]
        self.score = self.last_row[1]
        self.bflies = self.last_row[2]
        self.pigeons = self.last_row[3]
        self.highsc = max(self.scoreboard.iloc[:,1].tolist())
        self.highb = max(self.scoreboard.iloc[:,2].tolist())
        self.highp = max(self.scoreboard.iloc[:,3].tolist())

    #plots the personal score, the number of butterflies that were caught and the number of pigeons that were shot
    #also plots the highest scores
    def plot(self):
        '''
        plots the personal score, the number of butterflies that were caught and the number of pigeons that were shot
        also plots the highest scores
        '''
        self.axes[0].bar(5, self.score, tick_label = "Score", width = 0.3, color = '#77CEF0')
        self.axes[0].bar(5.7, self.highsc, width = 0.3,  color = '#CD5C5C')
        self.axes[1].bar(self.x, (self.bflies, self.pigeons), tick_label = self.tick_label,  color = '#77CEF0' )
        self.axes[1].bar(self.x2, (self.highb, self.highp), color = '#CD5C5C')
        self.fig.suptitle('Scoreboard of ' + self.name)
        self.axes[1].legend(["Your score", "Highscores"])

        plt.show()

"""