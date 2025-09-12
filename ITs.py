import random
import pygame
import math
class ITs:
    def __init__(self,y,x,health,list_of_caps,list_of_shirts,list_of_boots):
        self.y = y
        self.x = x
        self.health = health
        self.speed = 2 
        self.countdown = -5 

        self.IT_cap = list_of_caps[random.randint(0,len(list_of_caps)-1)]
        self.IT_shirt = list_of_shirts[random.randint(0,len(list_of_caps)-1)]
        self.IT_boot = list_of_boots[random.randint(0,len(list_of_caps)-1)]

        self.width = max(self.IT_cap.get_width(), self.IT_shirt.get_width(), self.IT_boot.get_width())
        self.height = self.IT_cap.get_height() + self.IT_shirt.get_height() + self.IT_boot.get_height()
        self.surface = pygame.Surface((self.width,self.height),pygame.SRCALPHA)

        self.surface.blit = (self.IT_cap,(0,0))
        self.surface.blit = (self.IT_shirt,(0,self.IT_cap.get_height()))
        self.surface.blit = (self.IT_boot,(0,self.IT_cap.get_height() + self.IT_shirt.get_height()))

    def move(self,player_x,player_y):
        angle = math.atan2(player_y - self.y, player_x - self.x)
        self.x += self.speed * math.cos(angle)
        self.y += self.speed * math.sin(angle)

    def death(self,ITs_list,screen):
        self.countdown += 1
        rotated_image = pygame.transform.rotate(self.surface, abs(self.countdown) * 10)
        screen.blit(rotated_image,(self.x+ abs(self.countdown)*2,self.y + self.countdown*2))
        if self.countdown >= 5:
                ITs_list.remove(self)

    def draw(self,screen,ITs_list):
        if self.health >= 0:
            screen.blit(self.surface,(self.x,self.y))
        else:
            self.death(ITs_list,screen)

    def attack(self,player_x,player_y,player_width,player_height,damage):
        if self.x - player_x < player_width and self.y - player_y < player_height:

            self.health -= damage