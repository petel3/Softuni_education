from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class Test_paint_factory(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory("Paints", 100)

    def test_initialization_all_attributes(self):
        self.assertEqual("Paints", self.factory.name)
        self.assertEqual(100, self.factory.capacity)
        self.assertListEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertDictEqual(self.factory.products, self.factory.ingredients)

    def test_add_ingredient_method_should_raise_exception_if_product_not_in_ingredients(self):
        self.factory.ingredients = {"white":10, "yellow":15}
        product_type = "roses"
        product_quantity = 15
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient(product_type, product_quantity)
        self.assertEqual(f"Ingredient of type {product_type} not allowed in PaintFactory", str(ex.exception))

    def test_can_add(self):
        self.factory.ingredients = {"white":10, "yellow":10}

        result1=self.factory.can_add(50)
        self.assertEqual(True, result1)

        result2 = self.factory.can_add(90)
        self.assertEqual(False, result2)

    def test_add_ingredient_raises_error_for_quantity_of_ingredient(self):
        self.factory.ingredients = {"white": 10, "yellow": 10}
        product_type = "white"
        product_quantity = 120
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient(product_type,product_quantity)
        self.assertEqual("Not enough space in factory",str(ex.exception))

    def test_add_ingredient_should_be_added_correctly(self):
        self.factory.ingredients = {"white": 10, "yellow": 10}
        product_type = "red"
        product_quantity = 10
        self.factory.add_ingredient(product_type, product_quantity)
        self.assertEqual({"white": 10, "yellow": 10,"red":10},self.factory.ingredients)

    def test_remove_ingredient_method_should_raise_exception_if_product_not_in_ingredients(self):
        self.factory.ingredients = {"white":10, "yellow":15}
        product_type = "roses"
        product_quantity = 15
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient(product_type, product_quantity)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredient_method_should_raise_exception_if_product_quantities_are_not_equal(self):
        self.factory.ingredients = {"white":10, "yellow":15}
        product_type = "white"
        product_quantity = 15
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient(product_type, product_quantity)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_method_should_work_correctly(self):
        self.factory.ingredients = {"white":10, "yellow":15}
        product_type = "white"
        product_quantity = 10
        self.factory.remove_ingredient(product_type,product_quantity)
        self.assertEqual({"white":0, "yellow":15}, self.factory.ingredients)

    def test_repr_method(self):
        self.factory.ingredients = {"Black": 10, "Red": 5}
        expect = f"Factory name: Paints with capacity {self.factory.capacity}.\n" + "Black: 10\n" + "Red: 5\n"
        self.assertEqual(expect, self.factory.__repr__())


if __name__ == "__main__":
    main
