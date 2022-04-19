from project.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price:float, milliliters:float):
        super().__init__(name, price, milliliters)