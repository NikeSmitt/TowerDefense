import pygame
import os

from menu.menu import Menu
from menu.menuImages import menu_images
from towers.archerTower import ArcherTower


class ArcherTowerShort(ArcherTower):

    def __init__(self, x, y):
        super().__init__(x, y)

        # load tower images
        # self.width = 90
        self.tower_images = self._load_tower_images()
        self.archer_images = self._load_archer_images()

        # differences
        self.range = 130
        self.original_range = self.range
        self.damage = 1
        self.original_damage = self.damage
        self.price = [2000, 5000]

        # define menu and buttons
        self.menu = Menu(self, self.x, self.y, menu_images.get_menu_bg(), self.price)
        self.menu.add_button(menu_images.get_upgrade_button(), "upgrade")


    def _load_tower_images(self):
        original_images = [pygame.image.load(os.path.join("game_assets/archer_towers/archerTowerShort", f"{x}.png")) for
                           x in range(7, 10)]
        # scale = (original_images[0].get_width() / original_images[0].get_height())
        return [pygame.transform.scale(img, (self.width, self.height)) for img in original_images][:]

    def _load_archer_images(self):
        original_images = [pygame.image.load(os.path.join("game_assets/archer_towers/archerTopShort", f"{x}.png")) for
                           x in range(38, 44)]
        return original_images[:]  # pygame.transform.scale(img, (32, 32))
