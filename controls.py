import pygame
from sys import exit as close_game


def event_loop(dino):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                dino.is_jump = True


def update(screen, background, dino):
    screen.blit(background, (0, 0))
    dino.update()
    dino.output()
    pygame.display.flip()