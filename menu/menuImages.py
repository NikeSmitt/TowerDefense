import os
import pygame


class MenuImages:

    def __init__(self):
        self._menu_bg = None
        self._upgrade_button = None
        self._star = None

    def _get_image(self, width, height, *args):
        img = pygame.image.load(os.path.join(*args))
        img = pygame.transform.scale(img, (width, height))
        return img

    def get_menu_bg(self, width=200, height=100):
        if self._menu_bg is None:
            self._menu_bg = self._get_image(width, height, 'game_assets', 'menu', 'menu.png')
        return self._menu_bg

    def get_upgrade_button(self, width=60, height=60):
        if self._upgrade_button is None:
            self._upgrade_button = self._get_image(width, height, 'game_assets', 'menu', 'upgrade.png')
        return self._upgrade_button

    def get_star(self, width=20, height=20):
        if self._star is None:
            self._star = self._get_image(width, height, 'game_assets', 'menu', 'star.png')
        return self._star


menu_images = MenuImages()
