import pygame
from sys import exit as close_game


def event_loop(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                close_game()
            elif event.key == pygame.K_SPACE:
                if game.dino.jumps < 2:
                    game.dino.image = pygame.image.load("img/dino_no_shadow.png")
                    game.dino.is_jump = True
                    game.dino.is_falling = False
                    game.dino.speed_y = 15
                    game.dino.jumps += 1


def update(game):
    game.screen.blit(game.background, (0, 0))
    game.road.update()
    game.road.output()
    game.dino.update()
    game.dino.output()
    game.enemies.update()
    game.enemies.spawn_enemy()
    #check_collisions(game)
    pygame.display.flip()


def check_collisions(game):
    if pygame.sprite.spritecollideany(game.dino, game.enemies.enemies):
        close_game()
