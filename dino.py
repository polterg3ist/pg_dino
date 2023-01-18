import pygame


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
        self.angle = 1

    def output(self):
        if self.jumps == 2:
            self.blit_rotate_dino(self.angle)
            self.angle += 10
        else:
            self.screen.blit(self.image, self.rect)

    def blit_rotate_dino(self, angle):
        rotated_image = pygame.transform.rotate(self.image, angle)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=self.rect.topleft).center)
        self.screen.blit(rotated_image, new_rect.topleft)

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
                self.angle = 1
