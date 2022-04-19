from project.car.car import Car


class Driver:
    def __init__(self,name):
        self.name = name
        self.car=Car if Car else None
        self.number_of_wins=0



    @property
    def name(self):
        return

    @name.setter
    def name(self, value):
        if value.Strip()=="":
            raise ValueError("Name should contain at least one character!")

