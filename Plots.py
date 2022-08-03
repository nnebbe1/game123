from matplotlib import pyplot as plt
import pandas as pd
from helper import *

#Plot class for creating a Plot at the end of the game that displays scores
class Plot():
    
    def __init__(self):
        self.x = [10, 15, 20]
        self.x2 = [10.7, 15.7, 20.7]
        self.score = 0
        self.bflies = 0
        self.pigeons = 0
        self.highsc = 0
        self.highb = 0
        self.highp = 0
        self.name = ''
        self.last_row = []
        self.color = RED
        self.tick_label = ["Score", "Butterflies", "Pigeons"]
        self.scoreboard = pd.read_csv('data\scoreboard.csv')
        print(self.scoreboard)
        self.fig, self.ax = plt.subplots(nrows = 1, ncols = 1)

    #sets the different scores to the correct numbers from the csv file         
    def set_scores(self):
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
        self.ax.bar(self.x, (self.score, self.bflies, self.pigeons), tick_label = self.tick_label,  color = '#77CEF0' )
        print(self.highb)
        self.ax.bar(self.x2, (self.highsc, self.highb, self.highp), color = '#77F077')
        #self.ax.xticks(self.x, self.tick_label)
        self.ax.set_title('Scoreboard of ' + self.name)
        self.ax.legend(["Your score", "Highscores"])

        plt.show()