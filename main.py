import pygame
import controls
from dino import Dino
from road import Road
from enemies import Enemies


class Game:
    def __init__(self):
        self.FPS = 60
        self.WIDTH = 800
        self.HEIGHT = 600
        self.DEBUG = True
        self.clock = pygame.time.Clock()
        #self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.SCALED | pygame.FULLSCREEN, vsync=1)
        pygame.display.set_caption("Parkour Dino")
        self.background = pygame.image.load("img/bg_5_pixart.png").convert()
        self.background = pygame.transform.smoothscale(self.background, self.screen.get_size())
        self.dino = Dino(self.screen, self.DEBUG)
        self.road = Road(self.screen)
        self.enemies = Enemies(self.screen, self.DEBUG)

    def run(self):
        pygame.init()
        while True:
            controls.event_loop(self)
            controls.update(self)
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = Game()
    app.run()

exit()
