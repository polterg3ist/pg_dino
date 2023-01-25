import pygame
from random import uniform
from cactus import Cactus
from time import time
from pygame.sprite import Group


class Enemies:
    def __init__(self, game):
        self.game = game
        self.enemies = Group()
        self.last = time()
        self.wait_time = 1

    def update(self):
        for enemy in self.enemies.copy():
            enemy.update()
            enemy.output()
            if enemy.rect.right <= self.game.screen_rect.left:
                self.enemies.remove(enemy)

    def spawn_enemy(self):
        now = time()
        delta = now - self.last
        if delta >= self.wait_time:
            enemy = Cactus(self.game)
            self.enemies.add(enemy)
            self.wait_time = uniform(1, 2.5)
            self.last = time()
