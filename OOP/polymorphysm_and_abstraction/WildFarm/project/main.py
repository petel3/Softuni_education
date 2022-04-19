from project.animals.birds import Owl, Hen
from project.animals.mammals import Dog
from project.food import Meat, Vegetable, Fruit

dog = Dog("Harry", 10, "Nebraska")

fruit = Fruit(5)
meat=Meat(5)
veg=Vegetable(4)
dog.feed(veg)
dog.feed(fruit)
dog.feed(meat)
print(dog.make_sound())
print(dog)

