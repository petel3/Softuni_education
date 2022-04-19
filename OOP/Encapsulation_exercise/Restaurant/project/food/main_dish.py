from project.food.food import Food


class MainDish(Food):
    def __init__(self, name, price:float, grams:float):
        super().__init__(name, price, grams)