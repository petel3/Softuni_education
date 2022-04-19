from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.driver import Driver


class Controller:
    def __init__(self):
        self.cars=[]
        self.drivers=[]
        self.races=[]

    def create_car(self,car_type: str, model: str, speed_limit: int):
        pass
        # for cars in self.cars:
        #     car = self.__create_car_by_type(car_type, model, speed_limit)
        #     if car.model==cars.model:
        #         raise Exception(f"Car {model} is already created!")
        #     else:
        #         self.cars.append(car)
        #         return f"{car_type} {model} is created."


    def create_driver(self,driver_name: str):
        pass
    #     if driver_name not in self.drivers:
    #         self.drivers.append(driver_name)
    #         return f"Driver {driver_name} is created."
    #     else:
    #         raise Exception(f"Driver {driver_name} is already created!")
    #
    # def create_race(self,race_name: str):
    #     if race_name not in self.races:
    #         self.races.append(race_name)
    #         return f"Race {race_name} is created."
    #     else:
    #         raise Exception(f"Race {race_name} is already created!")


    def add_car_to_driver(self,driver_name: str, car_type: str):
        pass
        # if driver_name not in self.drivers:
        #     raise Exception(f"Driver {driver_name} could not be found!")
        # else:
        #     for driver in self.drivers:
        #         for car in self.cars[::-1]:
        #             if not car:
        #                 raise Exception(f"Car {car_type} could not be found!")
        #
        #         return f"Driver {driver_name} chose the car {car.model}."

            #
            # return f"Driver {driver_name} changed his car from {old_model} to {new_model}."

    def add_driver_to_race(self,race_name: str, driver_name: str):
        pass
        # try:
        #     race=[r for r in self.races if r.name==race_name][0]
        # except:
        #     raise Exception(f"Race {race_name} could not be found!")
        # try:
        #     driver = [d for d in self.drivers if d.name == driver_name][0]
        # except:
        #     raise Exception(f"Driver {driver_name} could not be found!")
        #
        # if driver.car is None:
        #     raise Exception(f"Driver {driver_name} could not participate in the race!")
        # if driver not in race.drivers:
        #     return f"Driver {driver_name} added in {race_name} race."
        # else:
        #     return f"Driver {driver_name} is already added in {race_name} race."
        #
        #


    def start_race(self,race_name: str):
        pass

        # for race in self.races:
        #     if race.name!=race_name:
        #         raise Exception(f"Race {race_name} could not be found!")
        # if len(self.races)<3:
        #     raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        # else:
        #     driver=sorted([d for d in self.races],key=lambda d:d.car.speed_limit, reverse=True)[0]
        #     return f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}."
        #


    def __create_car_by_type(self,car_type,model,speed_limit):
        pass
        # if car_type=="MuscreCar":
        #     return MuscleCar(model,speed_limit)
        # elif car_type=="SportsCar":
        #     return MuscleCar(model,speed_limit)
        #
        # return None



