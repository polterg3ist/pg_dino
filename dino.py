import pygame
from random import choice


class Dino:
    def __init__(self, screen, debug):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.debug = debug
        self.image = pygame.image.load("img/dino_1.png")
        self.rect = self.image.get_rect()
        self.dino_animations = ["img/dino_1.png", "img/dino_2.png", "img/dino_1.png", "img/dino_3.png"]
        self.cur_anim = 0
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
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
            if not (self.is_jump or self.is_falling):
                self.image = pygame.image.load(self.dino_animations[self.cur_anim])
                self.screen.blit(self.image, self.rect)

                if pygame.time.get_ticks() % 2 == 0:
                    self.cur_anim += 1
                    if self.cur_anim == 4:
                        self.cur_anim = 0
            else:
                self.image = pygame.image.load("img/dino_no_shadow.png")
                self.screen.blit(self.image, self.rect)

            if self.debug:
                pygame.draw.rect(self.screen, (255, 0, 0), (*self.rect.topleft, *self.image.get_size()), 2)

    def blit_rotate_dino(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=self.rect.topleft).center)
        self.screen.blit(rotated_image, new_rect.topleft)
        if self.flip == "back-flip":
            self.angle += 10
        elif self.flip == "forward-flip":
            self.angle -= 10

        if self.debug:
            pygame.draw.rect(self.screen, (255, 0, 0), (*new_rect.topleft, *rotated_image.get_size()), 2)

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

            # Code below works when dino grounds
            if self.rect.bottom >= self.screen_rect.bottom:
                self.image = pygame.image.load("img/dino_1.png")
                self.is_falling = False
                self.speed_y = 15
                self.rect.bottom = self.screen_rect.bottom
                self.jumps = 0
                self.angle = 0
                self.flip = choice(self.flips)
