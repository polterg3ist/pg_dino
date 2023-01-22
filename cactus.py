import pygame
from random import choice


class Cactus:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.images = ["img/cactus_2.png", "img/cactus_3.png", "img/cactus_4.png"]
        self.image = pygame.image.load(choice(self.images))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.screen_rect.bottomright

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.centerx -= 3