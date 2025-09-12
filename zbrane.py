import pygame 
import math
import ITs from IT

class Zbrane:
    def __init__(self,damage,hit_place,hit_texture,typ_zbrane):
        self.damage = damage
        self.hit_place = hit_place
        self.hit_texture = hit_texture
        self.typ_zbrane = typ_zbrane 
        
    def show_range (self,screen,direction,player_x,player_y):
        rotated_hit_place = pygame.transform.rotate(self.hit_place, direction * 90)
        hit_place_rect = rotated_hit_place.get_rect(center=(player_x, player_y))
        screen.blit(rotated_hit_place, hit_place_rect)

    def attack (self,screen,direction,ITs,):
        rotated_hit_place = pygame.transform.rotate(self.hit_place, direction * 90)
        hit_place_mask = pygame.mask.from_surface(rotated_hit_place)

        for _ in ITs:
            if 0 <= ITs.x < hit_place_mask.get_size()[0] and 0 <= ITs.y  < hit_place_mask.get_size()[1]:
                ITs.health -self.damage
    