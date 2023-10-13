import pygame as pg
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными из корабля игрока"""
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load('images/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        # self.rect = pg.Rect(0, 0, settings.bullet_width,settings.bullet_height)
        # ^ для просто цветной пули

        # создание снаряда в позици 0,0
        self.rect.centerx = ship.rect.centerx  # пулю перемещаю к кораблю
        self.rect.top = ship.rect.top
        # позиция (координаты) снаряда хранятся как дробь
        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)  # делает картинку
        # pg.draw.rect(self.screen, self.color, self.rect)
        # ^ рисует цветной прямоугольник



