from asyncore import write
from lib2to3.pgen2.token import NEWLINE
import pygame

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

scoreboard_file = open("data\scoreboard.csv", "a", newline="")  
print(user_name)
writer = csv.writer(scoreboard_file)
writer.writerow([user_name])
writer.writerow('ass')
scoreboard_file.close()