import pygame
import math

class Hero:
    def __init__(self,x,y, width, height, health, speed):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.health = health
        self.speed = speed

    def move(self, keys, screen_x, screen_y):
        # Create a vector for movement
        move_vector = pygame.math.Vector2(0, 0)
        
        if keys[pygame.K_w]:
            move_vector.y -= 1
        if keys[pygame.K_s]:
            move_vector.y += 1
        if keys[pygame.K_a]:
            move_vector.x -= 1
        if keys[pygame.K_d]:
            move_vector.x += 1
        #kontroluje pokud jsou zmáčknutá dvě tlačítka najednou
        if move_vector.length() > 0:
            move_vector.normalize_ip()

        #násobení rychlostí
        self.x += move_vector.x * self.speed
        self.y += move_vector.y * self.speed
        
            
        if self.y >= screen_y- self.height:
            self.y = screen_y  - self.height
        if self.x >= screen_x- self.width:
            self.x = screen_x  - self.width
        if self.y <= 0:
            self.y = 0
        if self.x <= 0:
            self.x = 0
    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        center_x = self.x + self.width // 2
        center_y = self.y
        dx = mouse_x - center_x
        dy = mouse_y - center_y
        self.angle = math.degrees(math.atan2(dy, dx))

    def draw(self, surface, mouse_x, mouse_y):
    # Vytvoření povrchu pro postavu
        hero_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)# scralpha priprava na obrazek
        pygame.draw.rect(hero_surf, (255, 0, 0), (0, 0, self.width, self.height)) #vykresleni postavy
    # Otočení povrchu
        rotated_surf = pygame.transform.rotate(hero_surf, -self.angle)
    # Získání nových souřadnic pro vykreslení
        rect = rotated_surf.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        surface.blit(rotated_surf, rect.topleft)
    # Vykreslení čáry k myši
        pygame.draw.line(surface, (255, 0, 0), (self.x + self.width // 2, self.y), (mouse_x, mouse_y))