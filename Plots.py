import pygame as pg
from matplotlib import pyplot as plt
import Environment
from helper import *

class Plot():
    
    def __init__(self):
        self.x = []
        self.score = 0
        self.bflies = 0
        self.highsc = 0
        self.color = RED
        self.tick_label = ["Score", "Butterflies", "Highscore"]
        
    def update(s, b, h):
        self.score = s
        self.bflies = b
        self.highsc = h
        plt.bar(self.x, [self.score, self.bflies, self.highsc], color = self.color, tick_label = self.tick_label)
    