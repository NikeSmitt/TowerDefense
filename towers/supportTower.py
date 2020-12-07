import pygame
import os
from towers.tower import Tower


class SupportTower(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 150
        self.tower_images = None

    def _load_tower_images(self):
        pass

    def draw(self, win):
        super().draw_range_circle(win)
        super().draw(win)

    def support(self, towers):
        """
        will modify towers according to ability
        :param towers: list
        :return: None
        """
        pass