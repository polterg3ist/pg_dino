import pygame
from random import uniform
from cactus import Cactus
from time import time
from pygame.sprite import Group


class Enemies:
    def __init__(self, screen, debug):
        self.screen = screen
        self.debug = debug
        self.screen_rect = self.screen.get_rect()
        self.enemies = Group()
        self.last = time()
        self.wait_time = 1

    def update(self):
        for enemy in self.enemies.copy():
            enemy.update()
            enemy.output()
            if enemy.rect.right <= self.screen_rect.left:
                self.enemies.remove(enemy)

    def spawn_enemy(self):
        now = time()
        delta = now - self.last
        print(now, delta)
        if delta >= self.wait_time:
            enemy = Cactus(self.screen, self.debug)
            self.enemies.add(enemy)
            self.wait_time = uniform(1, 2.5)
            self.last = time()
