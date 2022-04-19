from unittest import TestCase,main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train=Train("Kiro",50)
    def test_train_initialization_atributes(self):
        self.assertEqual("Kiro",self.train.name)
        self.assertEqual(50, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_method_raise_exception_when_train_is_full(self):
        self.train.capacity=0
        with self.assertRaises(ValueError) as ex:
            self.train.add("Pesho")
        self.assertEqual(Train.TRAIN_FULL,str(ex.exception))

    def test_add_method_raise_exception_when_passenger_exists(self):
        self.train.passengers=["Pesho"]
        expected=f'Passenger {"Pesho"} Exists'
        with self.assertRaises(ValueError) as ex:
            self.train.add("Pesho")
        self.assertEqual(expected,str(ex.exception))

    def test_add_method_shuld_correctly_add_passanger(self):
        passanger="Kiro"
        self.assertEqual(Train.PASSENGER_ADD.format(passanger),self.train.add(passanger))

    def test_remove_method_raise_exception_if_not_passanger(self):
        passanger = "Kiro"
        passanger2 = "Miro"
        self.train.add(passanger)
        with self.assertRaises(ValueError) as ex:
            self.train.remove(passanger2)
        self.assertEqual(Train.PASSENGER_NOT_FOUND.format(passanger2),str(ex.exception))

    def test_remove_method_should_remove_correctly_passangers(self):
        passanger = "Kiro"

        self.train.add(passanger)

        self.assertEqual(Train.PASSENGER_REMOVED.format(passanger),self.train.remove(passanger))






if __name__=="__main__":
    main