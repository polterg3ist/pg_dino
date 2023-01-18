import pygame
import controls
from dino import Dino


def main():
    pygame.init()
    FPS = 60
    WIDTH = 800
    HEIGHT = 600
    start_ticks = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Parkour Dino")
    background = pygame.image.load("img/bg_4_pixart.jpg").convert()
    background = pygame.transform.smoothscale(background, screen.get_size())
    dino = Dino(screen)

    while True:
        controls.event_loop(dino)
        controls.update(screen, background, dino)
        clock.tick(FPS)


if __name__ == '__main__':
    main()

exit()
