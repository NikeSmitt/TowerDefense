import os
import pygame
from enemies.enemy import Enemy
from enemies.enemyImages import enemies_image

class Scorpion(Enemy):

    def __init__(self, width=64, height=64):
        super().__init__(width, height, 'Scorpion')

        self.images = enemies_image.get_scorpion_images()
        self.max_health = 1
        self.health = self.max_health



