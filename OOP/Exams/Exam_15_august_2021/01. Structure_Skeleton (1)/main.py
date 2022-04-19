from project.baked_food import baked_food
from project.baked_food.bread import Bread
from project.bakery import Bakery
from project.drink.tea import Tea
from project.table.table import Table

bread=Bread("White bread",1.5)
drink=Tea("Black tea",150,"Nestea")
table=Table(2,30)
table.reserve(15)
print(table.is_reserved)
table.reserve(15)
print(table.number_of_people)
print(bread)
table.order_food(bread)

table.order_drink(drink)
print(table.get_bill())



bakery=Bakery("Bace Kiko")
bakery.add_table("InsideTable",1,40)
bakery.table_repository.clear()
print((table.free_table_info()))
print(bakery.add_drink("Tea","Herbs tea",150.00,"Nestea"))
print(bakery.add_food("Bread","Tipov",2.00))
print(bakery.add_food("Bread","Pulnozurnest",1.00))
print(bakery.add_food("Cake","Tiramisu",5.00))
print(bakery.add_food("Cake","Biskvitena",3.00))
print(bakery.order_food(1,"Tipov","Pulnozurnest","Biskvitena"))
