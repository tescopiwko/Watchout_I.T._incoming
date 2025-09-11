import pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mask Touch Detection")

# Load image and create mask
image = pygame.image.load("sprite.png").convert_alpha()
mask = pygame.mask.from_surface(image)

# Get image size and center position
img_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Main loop
running = True
while running:
    screen.fill((30, 30, 30))
    screen.blit(image, img_rect.topleft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Convert global mouse position to local mask coordinates
            local_x = mouse_pos[0] - img_rect.x
            local_y = mouse_pos[1] - img_rect.y
            print(mask.get_size()[1])
            if 0 <= local_x < mask.get_size()[0] and 0 <= local_y < mask.get_size()[1]:
                if mask.get_at((local_x, local_y)):
                    print("Touched the mask!")
                else:
                    print("Clicked outside the visible area.")

    pygame.display.flip()

pygame.quit()
