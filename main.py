import pygame
from EP import Hero
from inventory import Template

screen_x = 1920 #800
screen_y = 1080 #600 
screen_color = "green"

screen = pygame.display.set_mode((screen_x, screen_y))
# aspekty HRÁČE
x = 1000
y = 500
width = 50
height = 50
health = 10
speed = 8
color = "red"
is_inventory_open = False

char_form = Template(430, 185, 300, 400) # ROZMĚRY gridu pro POSTAVU
#410 grid_x, 165 = grid_y
background_form = Template(screen_x/2-1100/2, screen_y/2-750/2, 1100, 750) # ROZMĚRY BACKGROUND gridu
gun_form = Template(750,285,200,200) # ROZMĚRY gridu pro ZBRAŇ
ammo_forms = [] # SEZNAM DO KTEREHO JSOU PRIDANY GRIDY PRO MUNICI
for i in range(4):# přidá se 4x 
    if i < 2:
        ammo_forms.append(Template(430 + i*160, 600, 140,140)) # 140x140 gridy pro munici -> VLOŽENÍ DO SEZNAMU (POKUD JE JICH V ŘADĚ MÉNĚ NEŽ 2)
    else:
        ammo_forms.append(Template(430 + i*160-2*160, 760, 140,140)) # 140x140 gridy pro munici -> VLOŽENÍ DO SEZNAMU
clothes_forms = [] # SEZNAM DO KTEREHO JSOU PRIDANY GRIDY PRO OBLEČENÍ
for i in range(3):
    clothes_forms.append(Template(970 + i*180, 285, 160,200)) # 140x140 gridy pro OBLEČENÍ -> VLOŽENÍ DO SEZNAMU

process_form = Template(750,505,740,395) # ROZMĚRY pro AKČNÍ grid

useless_forms = [] # SEZNAM pro gridy, které zatím nemají funkci (info prolly)
for i in range(2):
    useless_forms.append(Template(750 + i*380, 185, 360,80))
    
main_char = Hero(x,y, width, height, health, speed) # specifikace hrace - trida EP
running = True # SMYCKA HRY
clock = pygame.time.Clock()

while running:
    clock.tick(60) # omezeni na 60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                is_inventory_open = not is_inventory_open

    keys = pygame.key.get_pressed() # ziskani stisknutych klaves
    if keys[pygame.K_ESCAPE]:
        running = False # ukonceni hry pri stisknuti ESCAPE

    main_char.move(keys, screen_x, screen_y)
    # vykresleni na obrazovku
    screen.fill(screen_color) # vykreslení zelená barva pozadí
    main_char.draw(screen) # vykreslení hráče
    if is_inventory_open:
        background_form.draw(screen) # vykreslení provizorní grid pozadí
        
        char_form.draw(screen)  # vykreslení gridu na customizaci postavy
        for ammo_rect in ammo_forms:
            ammo_rect.draw(screen) # vykreslení vícero gridů pro munici
        
        gun_form.draw(screen) # vykreslení gridu pro ZBRAŇ
        for clothes_rect in clothes_forms:
            clothes_rect.draw(screen) # vykreslení vícero gridů pro OBLEČENÍ

        process_form.draw(screen) # vykreslení gridu pro AKČNÍ
        for useless_rect in useless_forms:
            useless_rect.draw(screen) # vykreslení vícero gridů pro NĚCO (zatím nefunkční)
    
        
        
    pygame.display.flip()
    