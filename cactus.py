import pygame
from random import choice


class Cactus(pygame.sprite.Sprite):
    def __init__(self, game):
        super(Cactus, self).__init__()
        self.game = game
        self.images = ["img/cactus_1.png", "img/cactus_2.png", "img/cactus_3.png"]
        self.random_image = choice(self.images)
        self.image = pygame.image.load(self.random_image)

        if self.random_image == "img/cactus_1.png":
            self.image = pygame.transform.scale(self.image, (70, 110))

        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.game.screen_rect.bottomright

    def output(self):
        self.game.screen.blit(self.image, self.rect)

        if self.game.DEBUG:
            pygame.draw.rect(self.game.screen, (255, 0, 0), (*self.rect.topleft, *self.image.get_size()), 2)

    def update(self):
        self.rect.centerx -= 5