import pygame
import os
from towers.archerTower import ArcherTower


class ArcherTowerShort(ArcherTower):

    def __init__(self, x, y):
        super().__init__(x, y)

        # load tower images
        self.tower_images = self._load_tower_images()
        self.archer_images = self._load_archer_images()

    def _load_tower_images(self):
        original_images = [pygame.image.load(os.path.join("game_assets/archer_towers/archerTowerShort", f"{x}.png")) for
                           x in range(7, 10)]
        return [pygame.transform.scale(img, (90, 90)) for img in original_images]

    def _load_archer_images(self):
        original_images = [pygame.image.load(os.path.join("game_assets/archer_towers/archerTopShort", f"{x}.png")) for
                           x in range(38, 44)]
        return original_images[:]  # pygame.transform.scale(img, (32, 32))
