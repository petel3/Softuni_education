class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.horse_power = horse_power
        self.fuel = fuel
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self,kilometers):
        required_fuel=kilometers*self.fuel_consumption
        if self.fuel>=required_fuel:
            self.fuel-=required_fuel
