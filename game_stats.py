class GameStats:
    """Отслеживание статистики игры"""
    def __init__(self, settings):
        """Инициализацируем статистику"""
        self.settings = settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Инициализирует статистику, которая обновляется в игре """
        self.ships_left = self.settings.ship_limit