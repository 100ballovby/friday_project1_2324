import pygame as pg


class Ship:
    def __init__(self, screen):
        """Инициализация корабля и установка его в нужную позицию на экране"""
        self.screen = screen

        # загрузим картинку корабля
        self.image = pg.image.load('images/ship.png')
        self.rect = self.image.get_rect()  # получаю колижн-модель корабля
        self.screen_rect = self.screen.get_rect()   # получаю границы экрана игры

        # каждый корабль будет появляться посередине экрана внизу
        self.rect.centerx = self.screen_rect.centerx  # центр по горизонтали корабля берется из центра экрана
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False  # по умолчанию он не двигается вправо

    def update(self):
        """Обновляет позицию корабля"""
        if self.moving_right:  # если двигаться вправо можно
            self.rect.centerx += 1

    def blitme(self):
        """Рисует корабль на экране игры"""
        self.screen.blit(self.image, self.rect)
