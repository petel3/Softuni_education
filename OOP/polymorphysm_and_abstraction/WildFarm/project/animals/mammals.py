from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ["Vegetable", "Fruit"]
    WEIGHT_MULTIPLIER = 0.1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"Squeak"


class Dog(Mammal):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_MULTIPLIER = 0.4

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"Woof!"


class Cat(Mammal):
    ALLOWED_FOODS = ["Meat", "Vegetable"]
    WEIGHT_MULTIPLIER = 0.3

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"Meow"


class Tiger(Mammal):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_MULTIPLIER = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"ROAR!!!"
