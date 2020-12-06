

class Tower:
    """
    Abstract class for towers
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 0
        self.width = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        self.menu = None
        self.tower_images = []
        self.damage = 1

    def draw(self, win):
        """
        Draws the tower
        :param win: surface
        :return: None
        """
        img = self.tower_images[self.level - 1]
        win.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

    def click(self, X, Y):
        """
        Returns if tower has been clicked on and
        selects tower if it was clicked
        :param X: int
        :param Y: int
        :return: bool
        """
        if self.x + self.width >= X >= self.x:
            if self.y + self.height >= Y >= self.y:
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
        self.level += 1
        self.damage += 1

    def get_upgrade_cost(self):
        """
        Returns the upgrade cost, if 0 then can't upgrade anymore
        :return: int
        """
        return self.price[self.level - 1]

    def move(self, x, y):
        self.x = x
        self.y = y

