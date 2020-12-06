import os
import pygame
from enemies.enemy import Enemy
from enemies.enemyImages import enemies_image

class Wizard(Enemy):
    NAME = 'Wizard'

    def __init__(self, width=64, height=64):
        super().__init__(width, height, 'Wizard')

        self.max_health = 3
        self.health = self.max_health
        self.images = enemies_image.get_wizard_images()


