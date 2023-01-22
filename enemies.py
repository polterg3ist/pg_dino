import pygame
from random import randint
from cactus import Cactus
from time import time


class Enemies:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.enemies = []
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
            enemy = Cactus(self.screen)
            self.enemies.append(enemy)
            self.wait_time = randint(1, 3)
            self.last = time()
