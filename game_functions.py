import sys
import pygame as pg


def check_events(ship):
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:  # если кто-то нажал на кнопку
            if event.key == pg.K_RIGHT:  # если это кнопка вправо
                ship.moving_right = True  # разрешаем кораблю двигаться вправо
        elif event.type == pg.KEYUP:  # если кнопку отпустили
            if event.key == pg.K_RIGHT:  # если это кнопка вправо
                ship.moving_right = False  # запрещаем кораблю двигаться вправо


def update_screen(settings, screen, ship):
    screen.fill(settings.bg_color)  # заливаем экран игры цветом
    ship.blitme()
    pg.display.flip()  # обновление кадров в игре
