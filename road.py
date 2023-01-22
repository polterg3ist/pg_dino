import pygame


class Road:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("img/road.png")
        self.image = pygame.transform.scale(self.image, (800, 100))

        self.rect1 = self.image.get_rect()
        self.rect1.bottomleft = self.screen_rect.bottomleft

        self.rect2 = self.image.get_rect()
        self.rect2.bottomleft = self.screen_rect.bottomright

        self.road_parts = [self.rect1, self.rect2]
        self.road_speed = 1

    def output(self):
        self.screen.blit(self.image, self.rect1)
        self.screen.blit(self.image, self.rect2)

    def update(self):
        for road in self.road_parts:
            road.centerx -= self.road_speed

            if road.right <= self.screen_rect.left:
                road.bottomleft = self.screen_rect.bottomright