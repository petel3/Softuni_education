from unittest import  TestCase,main

from project.vehicle import Vehicle


class Test_vehicle(TestCase):
    def test_vehicle_initializations(self):
        vehicle=Vehicle(100.00, 50.00)

        vehicle.capacity=150.00
        vehicle.fuel_consumption=1.25
        self.assertEqual(150.00,vehicle.capacity)
        self.assertEqual(100.00,vehicle.fuel)
        self.assertEqual(50.00,vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION,vehicle.fuel_consumption)

    def test_vehicle_driving_throws_exepction(self):
        vehicle = Vehicle(100.00, 50.00)
        with self.assertRaises(Exception) as ex:
            vehicle.drive(100)
        self.assertEqual("Not enough fuel",str(ex.exception))

    def test_vehicle_driving_decrease_fuel(self):
        vehicle = Vehicle(100.00, 50.00)
        vehicle.drive(1)

        result=98.75
        self.assertEqual(result,vehicle.fuel)

    def test_vehicle_refuel_raises_exeption(self):
        vehicle = Vehicle(100.00, 50.00)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(110)
        self.assertEqual("Too much fuel",str(ex.exception))

    def test_vehicle_is_refuel_increase_fuel(self):
        vehicle = Vehicle(100.00, 50.00)
        vehicle.capacity=150
        vehicle.refuel(5.00)
        self.assertEqual(105,vehicle.fuel)

    def test_vehicle_string_method(self):
        Vehicle.horse_power=100.15
        Vehicle.fuel_consumption=1.25
        Vehicle.fuel=50.15

        result=f"The vehicle has 100.15 " \
               f"horse power with 50.15 fuel left and 1.25 fuel consumption"
        self.assertEqual(result,Vehicle.__str__(Vehicle))
if __name__=="__main__":
    main