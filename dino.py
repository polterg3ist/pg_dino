import pygame


class Dino:
    def __init__(self, screen):
        self.image = pygame.image.load("img/dino_1_resized.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.speed_y = 15
        self.is_jump = False
        self.is_falling = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.is_jump:
            self.rect.centery -= self.speed_y
            self.speed_y -= 1

            if self.speed_y == 0:
                self.is_jump = False
                self.is_falling = True

        elif self.is_falling:
            self.rect.centery += self.speed_y
            self.speed_y += 1

            if self.rect.bottom >= self.screen_rect.bottom:
                self.is_falling = False
                self.speed_y = 15
                self.rect.bottom = self.screen_rect.bottom

