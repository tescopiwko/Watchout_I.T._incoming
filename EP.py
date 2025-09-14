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
       
    def draw(self, surface):
        pygame.draw.rect(surface,(255,0,0), (self.x, self.y, self.width, self.height))

        