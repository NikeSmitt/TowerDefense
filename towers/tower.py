import pygame


class Tower:
    """
    Abstract class for towers
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 90
        self.width = 90
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        self.tower_images = []
        self.damage = 1
        self.range = 1
        self.affected = False
        self.original_range = None
        self.original_damage = None
        self.selected = False

    def draw(self, win):
        """
        Draws the tower
        :param win: surface
        :return: None
        """
        img = self.tower_images[self.level - 1]
        win.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

    def draw_menu(self, win):
        if self.selected:
            self.menu.draw(win)

    def draw_range_circle(self, win):
        if self.selected:
            # draw range circle
            surface_circle = pygame.Surface((self.range * 2, self.range * 2)).convert_alpha()
            pygame.draw.circle(surface_circle, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            win.blit(surface_circle, (self.x - self.range, self.y - self.range))

    def click(self, x, y):
        """
        Returns if tower has been clicked on and
        selects tower if it was clicked
        :param x: int
        :param y: int
        :return: bool
        """

        # this need for move tower coordinates back because of drawing was with movement in 'draw(win)' method
        tower_img = self.tower_images[self.level - 1]
        tower_x = self.x - tower_img.get_width() // 2
        tower_y = self.y - tower_img.get_height() // 2

        if tower_x + self.width >= x >= tower_x:
            if tower_y + self.height >= y >= tower_y:
                return True
        return False

    def sell(self):
        """
        Call to sell the tower, returns sell price
        :return: int
        """
        return self.sell_price[self.level - 1]

    def upgrade(self):
        """
        Upgrades the tower for a given cost
        :return: None
        """
        self.level = min(self.level, len(self.price)) + 1
        self.damage = min(self.level, len(self.price)) + 1

    def get_upgrade_cost(self):
        """
        Returns the upgrade cost, if 0 then can't upgrade anymore
        :return: int
        """
        return self.price[self.level - 1]

    def move(self, x, y):
        self.x = x
        self.y = y
