import os
import pygame
from towers.tower import Tower
import time


class ArcherTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.archer_count = 0
        self.tower_images = []
        self.archer_images = []
        self.left = False
        self.range = 1
        self.in_range = False
        self.timer = time.time()

        # load tower images
        self.tower_images = []

        # load archer images

        self.archer_images = []

    def draw(self, win):

        super().draw_range_circle(win)

        # draw a tower
        super().draw(win)

        if self.in_range:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_images) * 10:
                self.archer_count = 0
        else:
            self.archer_count = 0

        archer = self.archer_images[self.archer_count // 10]
        if self.left:
            add = archer.get_width() - 9
        else:
            add = 25
        win.blit(archer, (self.x - add, self.y - archer.get_height() - 25))

    def change_range(self, new_range):
        """
        change range of archer tower
        :param new_range: int
        :return: None
        """
        self.range = new_range

    def attack(self, enemies):
        """
        Attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """
        self.in_range = False
        enemy_closest = []
        for enemy in enemies:
            x, y = enemy.x, enemy.y
            dist = ((x - self.x) ** 2 + (y - self.y) ** 2) ** 0.5
            if self.range >= dist:
                self.in_range = True
                enemy_closest.append(enemy)

        # flip archer to face to enemy
        enemy_closest.sort(key=lambda enemy_to_sort: enemy_to_sort.x)
        if len(enemy_closest):
            first_enemy = enemy_closest[0]

            # for lower enemies damages
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                if first_enemy.hit(self.damage):
                    enemy_closest.remove(first_enemy)

            if first_enemy.x < self.x and not self.left:
                self.left = True
                for x, img in enumerate(self.archer_images):
                    self.archer_images[x] = pygame.transform.flip(img, True, False)
            elif first_enemy.x > self.x and self.left:
                self.left = False
                for x, img in enumerate(self.archer_images):
                    self.archer_images[x] = pygame.transform.flip(img, True, False)



