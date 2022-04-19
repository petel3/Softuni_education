from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository=PlanetRepository()
        self.astronaut_repository=AstronautRepository()


    def add_astronaut(self,astronaut_type,name):

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        astronaut = self.__create_astronaut(astronaut_type, name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {astronaut.name}."



    def add_planet(self,name,items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet = Planet(name)
        planet.items=items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self,name):
        if self.astronaut_repository.find_by_name(name):
            astronaut = self.astronaut_repository.find_by_name(name)
            self.astronaut_repository.remove(astronaut)
            return f"Astronaut {astronaut.name} was retired!"
        raise Exception (f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen+=10


    def send_on_mission(self,planet_name):
        planet=self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")
        astronauts=self.astronaut_repository.prepare_austronauts_for_mission(5,30)
        if not astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")
        participated_astronauts=0
        for astronaut in astronauts:
            if len(planet.items)==0:
                break
            while astronaut.oxygen>0 and len(planet.items)>0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            participated_astronauts += 1
        if len(planet.items) == 0:
            return f"Planet: {planet_name} was explored. {participated_astronauts} astronauts participated in collecting items."
        else:
            return "Mission is not completed."





    def report(self):
        pass

    def __create_astronaut(self,astronaut_type,name):
        if astronaut_type=="Biologist":
            return Biologist(name)
        if astronaut_type=="Geodesist":
            return Geodesist(name)
        if astronaut_type=="Meteorologist":
            return Meteorologist(name)
        raise Exception("Astronaut type is not valid!")


