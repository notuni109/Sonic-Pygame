import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

sprite_sheet_image = pygame.image.load('graphics/eggman.png').convert_alpha()
# sprite_sheet_image = pygame.transform.flip(sprite_sheet_image, True, False)

frame0 = pygame.Surface((50, 48)).convert_alpha()
frame0.blit(sprite_sheet_image,(0, 0), (392, 46, 50, 48))

while True:
    screen.fill('Gray')
    screen.blit(frame0, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update() # update everything
    clock.tick(60) # max frame rate is 60FPS