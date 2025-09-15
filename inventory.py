import pygame

class Template:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = "white"

        self.border_color= "black"
        self.border_thickness = 5

    def draw(self, surface):
        pygame.draw.rect(surface, self.border_color, (self.x - self.border_thickness, self.y - self.border_thickness, self.width + 2 *self.border_thickness, self.height + 2* self.border_thickness))
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    