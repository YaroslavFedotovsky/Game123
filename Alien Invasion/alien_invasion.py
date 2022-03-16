import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание корабля
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль.
    bullets = Group()

    # Назначение цвета фона
    bg_color = (255, 153, 18)

    #Запуск основного цикла игры
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

        # При каждом проходе цикла перерисовывается экран
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()
run_game()