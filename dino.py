import pygame
from random import choice


class Dino:
    def __init__(self, screen):
        self.image = pygame.image.load("img/dino_1_resized.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.speed_y = 15
        self.jumps = 0
        self.is_jump = False
        self.is_falling = False
        self.angle = 0
        self.flips = ["back-flip", "forward-flip"]
        self.flip = choice(self.flips)

    def output(self):
        if self.jumps == 2:
            self.blit_rotate_dino()
        else:
            self.screen.blit(self.image, self.rect)

    def blit_rotate_dino(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=self.rect.topleft).center)
        self.screen.blit(rotated_image, new_rect.topleft)
        if self.flip == "back-flip":
            self.angle += 10
        elif self.flip == "forward-flip":
            self.angle -= 10

    def update(self):
        if self.is_jump:
            self.rect.centery -= self.speed_y
            self.speed_y -= 1

            if self.speed_y <= 0:
                self.is_jump = False
                self.is_falling = True

        elif self.is_falling:
            self.rect.centery += self.speed_y
            self.speed_y += 1

            if self.rect.bottom >= self.screen_rect.bottom:
                self.is_falling = False
                self.speed_y = 15
                self.rect.bottom = self.screen_rect.bottom
                self.jumps = 0
                self.angle = 0
                self.flip = choice(self.flips)
