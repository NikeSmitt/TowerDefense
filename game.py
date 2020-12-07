import pygame
import os
import sys
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard
from towers.archerTowerLong import ArcherTowerLong
from towers.archerTowerShort import ArcherTowerShort
from towers.rangeTower import RangeTower
from towers.damageTower import DamageTower

import time
import random

# 2:35:47
# https://www.youtube.com/watch?v=iLHAKXQBOoA&t=1945s


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.width = 1200
        self.height = int(self.width / (1920 / 1080))
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.attack_towers = [ArcherTowerShort(300, 300), ArcherTowerShort(950, 380), ArcherTowerLong(280, 450)]
        self.support_towers = [RangeTower(500, 100), DamageTower(500, 400)]
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.live_img = pygame.image.load(os.path.join("game_assets", 'heart.png'))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.path = [(15, 219), (144, 216), (191, 229), (230, 264), (526, 269), (581, 250), (616, 192), (630, 124),
                     (662, 73), (718, 55), (775, 65), (816, 102), (832, 151), (832, 151), (846, 204), (880, 246),
                     (932, 269), (983, 279), (1028, 312), (1046, 364), (1037, 419), (994, 468), (957, 480), (767, 483),
                     (724, 499), (683, 531), (164, 530), (115, 500), (91, 451), (77, 384), (39, 341), (6, 327),
                     (-20, 327)]
        self.timer = time.time()
        self.enemy_generate_time = random.randrange(1, 3) / 2
        self.life_font = pygame.font.SysFont('comicsans', 70)

    def run(self):
        run = True
        clock = pygame.time.Clock()
        FPS = 60

        while run:
            # generate enemies every preselected time:
            if time.time() - self.timer >= self.enemy_generate_time:
                self.timer = time.time()
                self.enemies.append(random.choice([Scorpion(), Wizard(), Club()]))
                self.enemy_generate_time = random.randrange(1, 3) / 2

            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # loop through attack towers
            for tower in self.attack_towers:
                tower.attack(self.enemies)

            # loop through support towers
            for tower in self.support_towers:
                tower.support(self.attack_towers)

            # loop through enemies and delete all enemies off the screen or run out health
            for enemy in self.enemies[:]:
                if enemy.x < -30:
                    self.lives -= 1
                    self.enemies.remove(enemy)
                elif enemy.health <= 0:
                    self.enemies.remove(enemy)
                    # del enemy

            if self.lives <= 0:
                run = False
                print("You Lose!!!")

            self.draw()

        pygame.quit()
        sys.exit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))

        # draw enemies
        for enemy in self.enemies:
            enemy.draw(self.win)

        # draw attack towers
        for tower in self.attack_towers:
            tower.draw(self.win)

        # draw support towers
        for tower in self.support_towers:
            tower.draw(self.win)

        # draw lives
        start_x = self.width - self.live_img.get_width() - 10
        text = self.life_font.render(str(self.lives), True, (0, 0, 0))
        self.win.blit(text, (start_x - text.get_width() - 10, 10))
        self.win.blit(self.live_img, (start_x, text.get_height() - self.live_img.get_height()))

        pygame.display.update()


g = Game()
g.run()
