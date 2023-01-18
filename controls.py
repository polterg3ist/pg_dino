import pygame
from sys import exit as close_game


def event_loop(dino):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if dino.jumps < 2:
                    dino.is_jump = True
                    dino.is_falling = False
                    dino.speed_y = 15
                    dino.jumps += 1


def update(screen, background, dino):
    screen.blit(background, (0, 0))
    dino.update()
    dino.output()
    pygame.display.flip()