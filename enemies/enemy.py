import math
import pygame


# 1:02:15


class Enemy:

    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.animation_count = 0
        self.vel = 3
        self.health = 1
        self.path = [(-20, 219), (64, 219), (144, 216), (191, 229), (230, 264), (526, 269), (581, 250), (616, 192), (630, 124),
                     (662, 73), (718, 55), (775, 65), (816, 102), (832, 151), (832, 151), (846, 204), (880, 246),
                     (932, 269), (983, 279), (1028, 312), (1046, 364), (1037, 419), (994, 468), (957, 480), (767, 483),
                     (724, 499), (683, 531), (164, 530), (115, 500), (91, 451), (77, 384), (39, 341), (6, 327), (-40, 327), (-1000, 327)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.path_pos = 0
        self.move_count = 0
        self.move_distance = 0
        self.dis = 0
        self.images = []
        self.max_health = 0
        self.name = name

        # used for flip image in case of moving in opposite direction ONLY ONCE!!!
        self.flipped = False

    def draw(self, win):
        """
        Draw the enemy with the given images
        :param win: surface
        :return: None
        """

        self.img = self.images[self.animation_count]
        self.animation_count += 1
        if self.animation_count > len(self.images) - 1:
            self.animation_count = 0
        win.blit(self.img, (self.x - self.width // 2, self.y - self.height))

        # draw a red circles along the enemy path
        # for point_x, point_y in self.path:
        #     pygame.draw.circle(win, (255, 0, 0), (point_x, point_y), 5)
        self.draw_health_bar(win)
        self.move()

    def draw_health_bar(self, win):
        """
        draw health bar above the enemy
        :param win: surface
        :return: None
        """
        length = 50
        move_by = round(length / self.max_health)
        health_bar = move_by * self.health

        health_bar_pos = self.x - self.img.get_width() // 2, self.y - self.img.get_height() - 10
        pygame.draw.rect(win, (255, 0, 0), (health_bar_pos[0], health_bar_pos[1], length, 10))
        pygame.draw.rect(win, (0, 255, 0), (health_bar_pos[0], health_bar_pos[1], health_bar, 10))

    def collide(self, X, Y):
        """
        Returns if position has hit enemy
        :param X: int
        :param Y: int
        :return: Bool
        """
        if self.x + self.width >= X >= self.x:
            if self.y + self.health >= Y >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: None
        """

        x1, y1 = self.path[self.path_pos]

        if self.path_pos + 1 >= len(self.path) - 2:
            x2, y2 = (-50, 355)
        else:
            x2, y2 = self.path[self.path_pos + 1]

        # move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        direction = (x2 - x1, y2 - y1)
        length = math.sqrt(direction[0] ** 2 + direction[1] ** 2)
        try:
            direction = (direction[0] / length, direction[1] / length)
        except ZeroDivisionError:
            direction = (x2 - x1, y2 - y1)

        if direction[0] < 0 and not self.flipped:
            for i, img in enumerate(self.images):
                self.flipped = True
                self.images[i] = pygame.transform.flip(img, True, False)

        move_x, move_y = self.x + direction[0], self.y + direction[1]
        # self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)

        self.x = move_x
        self.y = move_y

        # Go to next point
        if direction[0] >= 0:  # moving right
            if direction[1] >= 0:  # moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else:
            if direction[1] >= 0:  # moving down
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1

    def hit(self, damage):
        """
        Returns if an enemy has died and removes one health each call
        :param damage: int
        :return: Bool
        """
        self.health -= damage
        if self.health <= 0:
            return True
        return False

    # def __del__(self):
    #     print(f"***** {self.name} deleted *****")
