from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.5

    def __init__(self, name, caffeine: float):
        super().__init__(name, self.MILLILITERS, self.PRICE)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
