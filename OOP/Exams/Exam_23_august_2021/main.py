from project.astronaut.meteorologist import Meteorologist
from project.space_station import SpaceStation

space_station=SpaceStation()
print(space_station.add_astronaut("Meteorologist","Gosho"))
print(space_station.add_astronaut("Meteorologist","Gosho"))
print(space_station.add_astronaut("Meteorologist","Pesho"))
print(space_station.retire_astronaut("Gosho"))
print(space_station.retire_astronaut("Gosho"))
space_station.add_astronaut("Meteorologist","Gosho")

print(Meteorologist.__name__)
#
# astronaut1=SpaceStation.add_astronaut("Meteorologist","Gosho")
# astronaut2=SpaceStation.add_astronaut("Geodesist","Pesho")
# astronaut3=SpaceStation.add_astronaut("Meteorologist","Pesho")