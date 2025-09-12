import random
import pygame
class ITs:
    def __init__(self,y,x,health,list_of_caps,list_of_shirts,list_of_boots):
        self.y = y
        self.x = x
        self.health = health
        self.speed = 2 
        self.IT_cap = list_of_caps[random.randint(0,len(list_of_caps)-1)]
        self.IT_shirt = list_of_shirts[random.randint(0,len(list_of_caps)-1)]
        self.IT_boot = list_of_boots[random.randint(0,len(list_of_caps)-1)]4
    
    def move(self,player_x,player_y):
        