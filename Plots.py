from matplotlib import pyplot as plt
import pandas as pd
from helper import *

#Plot class for creating a Plot at the end of the game that displays scores
class Plot():
    
    def __init__(self):
        self.x = [10, 20, 30, 40]
        self.score = 0
        self.bflies = 0
        self.highsc = 0
        self.pigeons = 0
        self.name = ''
        self.last_row = []
        self.color = RED
        self.tick_label = ["Score", "Butterflies", "Pigeons", "Highscore"]
        self.scoreboard = pd.read_csv('scoreboard.csv')
        self.fig, self.ax = plt.subplots(nrows = 1, ncols = 1)

    #sets the different scores to the correct numbers from the csv file         
    def set_scores(self):
        self.last_row = self.scoreboard.iloc[-1].tolist()
        self.name = self.last_row[0]
        self.score = self.last_row[1]
        self.bflies = self.last_row[2]
        self.pigeons = self.last_row[3]
        self.highsc = self.scoreboard.iloc[:,1].max()

    #plots the personal score, the number of butterflies that were caught and the number of pigeons that were shot
    #also plots the highscore
    def plot(self):
        self.ax.bar(self.x, (self.score, self.bflies, self.pigeons, self.highsc), color = self.color, tick_label = self.tick_label )
        self.ax.set_title('Scoreboard of' + self.name)

        plt.show()