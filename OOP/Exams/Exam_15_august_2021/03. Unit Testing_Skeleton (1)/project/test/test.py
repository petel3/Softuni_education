from project.pet_shop import PetShop
from unittest import TestCase, main


class Test(TestCase):
    def setUp(self) -> None:
        self.petshop= PetShop("Sharo")
    def test_all_atributes_in_initialization(self):

        self.assertEqual("Sharo", self.petshop.name)
        self.assertEqual({},self.petshop.food)
        self.assertEqual([],self.petshop.pets)

    def test_add_food_raise_exeption_for_quantity(self):
        self.petshop.food={"Petfood":10}
        with self.assertRaises(ValueError) as ex:
            self.petshop.add_food("Petfood",0)
        self.assertEqual('Quantity cannot be equal to or less than 0',str(ex.exception))

    def test_add_food_when_name_not_in_petshop_expect_to_add_it(self):
        name="Petfood"
        name2 = "Petfoods"
        self.petshop.food={"Petfood":10}
        self.assertEqual(1, len(self.petshop.food))
        self.petshop.add_food(name, 5)
        self.petshop.add_food(name2, 5)
        self.assertEqual(15,self.petshop.food[name])
        self.assertEqual(5, self.petshop.food[name2])


    def test_add_food_when_food_and_quantity_are_correct(self):
        self.petshop.food = {"Petfood":0}
        name="Petfood"
        quantity=200
        self.assertEqual(f"Successfully added {quantity:.2f} grams of {name}.",self.petshop.add_food(name,200))

    def test_add_pet__method_check_if_appends_new_pet(self):
        self.petshop.add_pet("Sharko")
        name="Sharo"
        self.assertEqual(1,len(self.petshop.pets))
        self.assertEqual(f"Successfully added {name}.",self.petshop.add_pet(name))

    def test_add_pet__method_check_if_raises_error_from_adding_same_pet(self):
        name="Sharo"
        self.petshop.add_pet(name)
        with self.assertRaises(Exception) as ex:
            self.petshop.add_pet(name)
        self.assertEqual("Cannot add a pet with the same name",str(ex.exception))

    def test_feed_pet_method_raise_exeption_if_not_already_pet(self):
        name="Sharo"
        food_name="food"
        self.petshop.add_food(food_name,200)
        with self.assertRaises(Exception) as ex:
            self.petshop.feed_pet(food_name,name)
        self.assertEqual("Please insert a valid pet name",str(ex.exception))

    def test_feed_pet_method_return_msg_if_not_contain_food(self):
        name = "Sharo"
        self.petshop.add_pet(name)
        food_name = "food"
        self.assertEqual(f'You do not have {food_name}',self.petshop.feed_pet(food_name,name))

    def test_feed_pet_method_return_msg_is_adding_food(self):
        name = "Sharo"
        self.petshop.add_pet(name)
        food_name = "food"
        self.petshop.add_food(food_name, 50)
        self.assertEqual(f"Adding food...",self.petshop.feed_pet(food_name,name))
        self.assertEqual(1050,self.petshop.food[food_name])

    def test_feed_pet_method_return_feeding_pet(self):
        name = "Sharo"
        self.petshop.add_pet(name)
        food_name = "food"
        self.petshop.add_food(food_name, 500)
        self.assertEqual(f"{name} was successfully fed",self.petshop.feed_pet(food_name,name))
        self.assertEqual(400,self.petshop.food[food_name])

    def test_repr_method(self):
        expected=f'Shop {self.petshop.name}:\n' f'Pets: {", ".join(self.petshop.pets)}'
        self.assertEqual(expected,self.petshop.__repr__())

if __name__ == '__main__':
    main
