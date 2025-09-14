import pygame

class Hero:
    def __init__(self,x,y, width, height, health, speed):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.health = health
        self.speed = speed

    def move(self, keys, screen_x, screen_y):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        
            
        if self.y >= screen_y- self.height:
            self.y = screen_y  - self.height
        if self.x >= screen_x- self.width:
            self.x = screen_x  - self.width
        if self.y <= 0:
            self.y = 0
        if self.x <= 0:
            self.x = 0
        print(self.x,self.y, self.speed)

    def draw(self, surface):
        pygame.draw.rect(surface,(255,0,0), (self.x, self.y, self.width, self.height))

        