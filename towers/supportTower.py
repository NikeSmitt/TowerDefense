import pygame
import os
from towers.tower import Tower


class SupportTower(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 100
        self.tower_images = []
        # amount of rise towers damage or range

    def _load_tower_images(self):
        pass

    def draw(self, win):
        super().draw_range_circle(win)
        super().draw(win)

    def supported_towers(self, towers):
        """
        will add towers to modify them according to ability in support(towers) method
        :param towers: list
        :return: None
        """
        # towers which are within support tower range
        supported_towers = []
        for tower in towers:
            x = tower.x
            y = tower.y

            distance = ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5

            if distance <= self.range + tower.width:
                if not tower.affected:
                    supported_towers.append(tower)
                    tower.affected = True
            else:
                tower.affected = False
                tower.range = tower.original_range
                tower.damage = tower.original_damage
        return supported_towers

    def support(self, towers):
        """
        modify towers
        :param towers: list
        :return: None
        """
        pass
