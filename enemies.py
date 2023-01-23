import pygame
from random import randint
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
        delta = int(now - self.last)
        print(now, delta)
        if delta >= self.wait_time:
            enemy = Cactus(self.screen, self.debug)
            self.enemies.add(enemy)
            self.wait_time = randint(1, 3)
            self.last = time()
