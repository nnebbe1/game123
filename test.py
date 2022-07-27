from asyncore import write
from lib2to3.pgen2.token import NEWLINE
import pygame
from prompt_toolkit import prompt

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
user_name = user_name_input()   
print(user_name)
writer = csv.writer(scoreboard_file)
writer.writerow(user_name)
scoreboard_file.close()