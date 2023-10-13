import pygame as pg
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    ai_settings = Settings()

    pg.init()  # инициализируем pygame
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # создаем экран игры разрешением 1280х720px
    pg.display.set_caption("Alien Invasion")  # название окна игры

    ship = Ship(ai_settings, screen)
    bullets = Group()

    while True:  # цикл игры
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()  # применяю метод update ко ВСЕМ ПУЛЯМ В ГРУППЕ
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()  # вызываем игровую функцию
