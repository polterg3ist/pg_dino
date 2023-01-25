import pygame
from time import sleep


def event_loop(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:

            if game.lose or game.paused:
                if event.key == pygame.K_SPACE:
                    again(game)
                elif event.key == pygame.K_RETURN:
                    game.play = False
                elif event.key == pygame.K_ESCAPE:
                    game.paused = False
            else:
                if event.key == pygame.K_ESCAPE:
                    pause(game)
                elif event.key == pygame.K_SPACE:
                    if game.dino.jumps < 2:
                        game.dino.image = pygame.image.load("img/dino_no_shadow.png")
                        game.dino.is_jump = True
                        game.dino.is_falling = False
                        game.dino.speed_y = 15
                        game.dino.jumps += 1


def update(game):
    if not game.paused and not game.lose:
        game.screen.blit(game.background, (0, 0))
        game.road.update()
        game.road.output()
        game.dino.update()
        game.dino.output()
        game.enemies.update()
        game.enemies.spawn_enemy()
        check_collisions(game)
        show_fps(game)
    pygame.display.flip()


def check_collisions(game):
    if pygame.sprite.spritecollideany(game.dino, game.enemies.enemies):
        lose(game)


def show_fps(game):
    if game.DEBUG:
        font = pygame.font.SysFont('serif', 40)
        text = font.render(f"FPS-{int(game.clock.get_fps())}", True, (155, 0, 0))
        place = text.get_rect(topleft=(0, 0))
        game.screen.blit(text, place)


def again(game):
    game.lose = False
    game.paused = False
    game.score = 0
    game.enemies.enemies.empty()


def pause(game):
    game.paused = True
    # Pause caption
    font1 = pygame.font.SysFont('serif', 35)
    text1 = font1.render('PAUSE', True, (0, 100, 55))
    place = text1.get_rect(center=game.screen_rect.center)
    game.screen.blit(text1, place)

    font2 = pygame.font.SysFont('serif', 25)

    text2 = font2.render('again--SPACE', True, (0, 0, 0))
    text3 = font2.render('close--ESCAPE', True, (0, 0, 0))
    text4 = font2.render('quit--ENTER', True, (0, 0, 0))

    place1 = text2.get_rect(center=(place.centerx, place.centery + place.height))
    place2 = text3.get_rect(center=(place1.centerx, place1.centery + place1.height))
    place3 = text4.get_rect(center=(place2.centerx, place2.centery + place2.height))

    game.screen.blit(text2, place1)
    game.screen.blit(text3, place2)
    game.screen.blit(text4, place3)


def lose(game):
    game.lose = True
    # Lose caption
    font1 = pygame.font.SysFont('serif', 35)
    text1 = font1.render('LOSE', True, (0, 100, 55))
    place = text1.get_rect(center=game.screen_rect.center)
    game.screen.blit(text1, place)

    font2 = pygame.font.SysFont('serif', 25)
    text2 = font2.render('again--SPACE', True, (0, 0, 0))
    text3 = font2.render('quit--ENTER', True, (0, 0, 0))

    place1 = text2.get_rect(center=(place.centerx, place.centery + place.height))
    place2 = text3.get_rect(center=(place1.centerx, place1.centery + place1.height))

    game.screen.blit(text2, place1)
    game.screen.blit(text3, place2)
    # Stopping the program to evade SPACE miss click
    pygame.display.flip()
    sleep(0.5)
