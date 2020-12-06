import pygame
import os
from towers.archerTower import ArcherTower


class ArcherTowerLong(ArcherTower):

    def __init__(self, x, y):
        super().__init__(x, y)

        # load tower images
        self.tower_images = self._load_tower_images()
        self.archer_images = self._load_archer_images()

        # differences
        self.range = 200

    def _load_tower_images(self):
        original_images = [pygame.image.load(os.path.join("game_assets/archer_towers/archerTowerLong", f"{x}.png")) for
                           x in range(1, 3)]
        return [pygame.transform.scale(img, (90, 90)) for img in original_images]

    def _load_archer_images(self):
        original_images = [pygame.image.load(os.path.join("game_assets/archer_towers/archerTopLong", f"{x}.png")) for
                           x in range(64, 70)]
        return original_images[:]  # pygame.transform.scale(img, (32, 32))