from menu.menu import Menu
from menu.menuImages import menu_images
from towers.supportTower import SupportTower
import pygame
import os


class DamageTower(SupportTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 100
        self.effect = [1, 2]
        self.tower_images = self._load_tower_images()

        # differences
        self.price = [5000]

        # define menu and buttons
        self.menu = Menu(self, self.x, self.y, menu_images.get_menu_bg(), self.price)
        self.menu.add_button(menu_images.get_upgrade_button(), "upgrade")

    def _load_tower_images(self):
        original_images = [pygame.image.load(os.path.join("game_assets", "support_towers", "damage_towers", f"{x}.png"))
                           for
                           x in range(1, 3)]
        scale = (original_images[0].get_width() / original_images[0].get_height())
        return [pygame.transform.scale(img, (90, int(90 * scale))) for img in original_images]

    def support(self, towers):
        supported_towers = self.supported_towers(towers)
        for tower in supported_towers:
            tower.damage = tower.damage + self.effect[self.level - 1]
