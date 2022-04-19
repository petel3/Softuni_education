from unittest import  TestCase,main

from project.mammal import Mammal


class mammal_tests(TestCase):


    def test_is_mammal_initialized_correct(self):
        mammal = Mammal("Tom", "Cat", "Meow")
        self.assertEqual("Tom",mammal.name)
        self.assertEqual("Cat",mammal.type)
        self.assertEqual("Meow",mammal.sound)
        self.assertEqual("animals",mammal._Mammal__kingdom)
    def test_is_mammal_make_sound(self):
        mammal = Mammal("Tom", "Cat", "Meow")

        expected=f"{mammal.name} makes {mammal.sound}"
        actual=mammal.make_sound()
        self.assertEqual(expected,actual)

    def test_is_mammal_return_kingdom(self):
        mammal = Mammal("Tom", "Cat", "Meow")
        expected="animals"
        actuial=mammal.get_kingdom()
        self.assertEqual(expected,actuial)

    def test_is_mammal_return_info(self):
        mammal = Mammal("Tom", "Cat", "Meow")
        expected=f"{mammal.name} is of type {mammal.type}"
        actual=mammal.info()
        self.assertEqual(expected,actual)


if __name__=="__main__":
    main