import pygame
import controls
from dino import Dino
from road import Road
from enemies import Enemies
from sys import exit


class Game:
    def __init__(self):
        self.FPS = 60
        self.WIDTH = 800
        self.HEIGHT = 600
        self.DEBUG = False
        self.VSYNC = True
        self.paused = False
        self.play = True
        self.lose = False
        self.score = 0
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.SCALED | pygame.FULLSCREEN, vsync=self.VSYNC)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Parkour Dino")
        self.background = pygame.image.load("img/bg_5_pixart.png").convert()
        self.background = pygame.transform.smoothscale(self.background, self.screen.get_size())
        self.dino = Dino(self)
        self.road = Road(self)
        self.enemies = Enemies(self)

    def run(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        while self.play:
            controls.event_loop(self)
            controls.update(self)
            self.clock.tick(self.FPS)
        exit()


if __name__ == '__main__':
    app = Game()
    app.run()

exit()
