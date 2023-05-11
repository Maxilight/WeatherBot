import sys

import pygame
pygame.init()
W = 500
H = 500
screen = pygame.display.set_mode((W, H))
fps = 60
clock = pygame.time.Clock()


surf_comp = pygame.Surface((50, 50))
surf_comp.fill((255, 155, 0))
rect_comp = surf_comp.get_rect()
rect_comp.x = 300
rect_comp.y = 300

surf_user = pygame.Surface((50, 50))
surf_user.fill((155, 0, 255))
rect_user = surf_user.get_rect()
rect_user.x = 50
rect_user.y = 50
spriteX = screen.get_width()
spriteY = screen.get_height()


left = False
right = False
up = False
down = False

pygame.display.update()
while True:
    screen.fill((0, 0, 0))

    screen.blit(surf_comp, rect_comp)
    screen.blit(surf_user, rect_user)
    clock.tick(fps)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        rect_user.x += 5
        left = False
        right = True
        up = False
        down = False
    if key[pygame.K_LEFT]:
        rect_user.x -= 5
        left = True
        right = False
        up = False
        down = False
    if key[pygame.K_UP]:
        rect_user.y -= 5
        left = False
        right = False
        up = True
        down = False
    if key[pygame.K_DOWN]:
        rect_user.y += 5
        left = False
        right = False
        up = False
        down = True


    if rect_user.x < rect_comp.x and rect_user.colliderect(rect_comp) and right:
        rect_comp.x += 5
    elif rect_user.x > rect_comp.x and rect_user.colliderect(rect_comp) and left:
        rect_comp.x -= 5
    elif rect_user.y > rect_comp.y and rect_user.colliderect(rect_comp) and up:
        rect_comp.y -= 5
    elif rect_user.y < rect_comp.y and rect_user.colliderect(rect_comp) and down:
        rect_comp.y += 5



    pygame.display.update()

