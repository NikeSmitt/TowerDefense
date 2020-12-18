import os
import pygame
from enemies.enemy import Enemy
from enemies.enemyImages import enemies_image


class Club(Enemy):

    def __init__(self, width=64, height=64):
        super().__init__(width, height, 'Club')

        self.max_health = 10
        self.health = self.max_health
        self.images = enemies_image.get_club_images()
