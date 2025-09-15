import pygame
from EP import Hero
from inventory import Template

screen_x = 1920 #800
screen_y = 1080 #600 
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

char_form = Template(430, 185, 300, 400)
#410 grid_x, 165 = grid_y
background_form = Template(screen_x/2-1100/2, screen_y/2-750/2, 1100, 750)
ammo_forms = []
for i in range(4):
    if i < 2:
        ammo_forms.append(Template(430 + i*160, 600, 140,140))
    else:
        ammo_forms.append(Template(430 + i*160-2*160, 760, 140,140))

    
main_char = Hero(x,y, width, height, health, speed)
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    main_char.move(keys, screen_x, screen_y)
    screen.fill(screen_color)
    background_form.draw(screen)
    
    char_form.draw(screen)
    for ammo_rect in ammo_forms:
        ammo_rect.draw(screen)
    
        
    main_char.draw(screen)
        
        
    
    
    pygame.display.flip()
    