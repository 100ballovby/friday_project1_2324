import sys
import pygame as pg


def check_keydown_events(event, ship):
    """Отслеживает нажатие клавиш"""
    if event.key == pg.K_RIGHT:  # если это кнопка вправо
        ship.moving_right = True  # разрешаем кораблю двигаться вправо
    if event.key == pg.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш"""
    if event.key == pg.K_RIGHT:  # если это кнопка вправо
        ship.moving_right = False  # запрещаем кораблю двигаться вправо
    if event.key == pg.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:  # если кто-то нажал на кнопку
            check_keydown_events(event, ship)
        elif event.type == pg.KEYUP:  # если кнопку отпустили
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship):
    screen.fill(settings.bg_color)  # заливаем экран игры цветом
    ship.blitme()
    pg.display.flip()  # обновление кадров в игре
