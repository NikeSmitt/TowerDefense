import os
import pygame
from towers.supportTower import SupportTower


class RangeTower(SupportTower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 150
        self.tower_images = self._load_tower_images()

    def _load_tower_images(self):
        original_images = [pygame.image.load(os.path.join("game_assets", "support_towers", "range_towers", f"{x}.png"))
                           for
                           x in range(1, 3)]
        scale = (original_images[0].get_width() / original_images[0].get_height())
        return [pygame.transform.scale(img, (90, int(90 / scale))) for img in original_images]
