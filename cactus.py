import pygame
from random import choice


class Cactus(pygame.sprite.Sprite):
    def __init__(self, screen, debug):
        super(Cactus, self).__init__()
        self.screen = screen
        self.debug = debug
        self.screen_rect = screen.get_rect()
        self.images = ["img/cactus_1.png", "img/cactus_2.png", "img/cactus_3.png"]
        self.random_image = choice(self.images)
        self.image = pygame.image.load(self.random_image)

        if self.random_image == "img/cactus_1.png":
            self.image = pygame.transform.scale(self.image, (70, 110))

        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.screen_rect.bottomright

    def output(self):
        self.screen.blit(self.image, self.rect)

        if self.debug:
            pygame.draw.rect(self.screen, (255, 0, 0), (*self.rect.topleft, *self.image.get_size()), 2)

    def update(self):
        self.rect.centerx -= 5