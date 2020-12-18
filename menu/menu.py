import os
import pygame
from menu.menuImages import menu_images


class Button:
    def __init__(self, x, y, img, name):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()

        pygame.font.init()
        self.font = pygame.font.SysFont('comicsans', 20)

    def click(self, x, y):
        """
        check is clicking was on the menu
        :param x: int
        :param y: int
        :return: Bool
        """
        if self.x + self.width >= x >= self.x:
            if self.y + self.height >= y >= self.y:
                return True
        return False

    def draw(self, win, tower, menu):
        win.blit(self.img, (self.x, self.y))
        # draw a star with cost
        win.blit(menu_images.get_star(), (self.x, self.y + self.img.get_height()))
        text = self.font.render(str(menu.item_costs[tower.level - 1] if tower.level <= len(menu.item_costs) else 'MAX'), True, (255, 255, 255))
        win.blit(text, (self.x + menu_images.get_star().get_width() + 5,
                        self.y + self.img.get_height() + menu_images.get_star().get_width() / 3))


class Menu:
    """
    menu for holding items
    """

    def __init__(self, tower, x, y, img, costs):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_names = []
        self.item_costs = costs
        self.buttons = []
        self.items = 0
        self.bg_img = img
        self.tower = tower

    def get_clicked(self, x, y):
        """
        return the clicked item from menu
        :param x:
        :param y:
        :return: str
        """

        for button in self.buttons:
            if button.click(x, y):
                return button.name

    def draw(self, win):
        """
        draw menu bg and buttons
        :param win:
        :return:
        """
        win.blit(self.bg_img, (self.x, self.y))
        for button in self.buttons:
            button.draw(win, self.tower, self)


    def add_button(self, image, name):
        """

        :param image:
        :param name:
        :return:
        """

        button_x = self.x + 10 + (image.get_width() + 10) * self.items
        button_y = self.y + 10
        self.items += 1
        self.buttons.append(Button(button_x, button_y, image, name))


