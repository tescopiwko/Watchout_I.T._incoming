import pygame
from test_EP import Hero

screen_x = 800
screen_y = 600
screen_color = "green"

screen = pygame.display.set_mode((screen_x, screen_y))
#hrac
x = 1000
y = 500
width = 50
height = 50
health = 10
speed = 8
color = "red"

main_char = Hero(x,y, width, height, health, speed)
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    main_char.move(keys, screen_x, screen_y)
    screen.fill(screen_color)
    main_char.draw(screen)
    
    pygame.display.flip()
    