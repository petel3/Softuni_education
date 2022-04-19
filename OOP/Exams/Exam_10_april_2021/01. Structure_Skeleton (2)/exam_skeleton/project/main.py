from project.aquarium.base_aquarium import BaseAquarium
from project.decoration.base_decoration import BaseDecoration
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

base_aquarium=BaseAquarium("Aquram",50)
fresh_water_fish=FreshwaterFish("Kiro","FreshwaterFish",10)
salt_waret=SaltwaterFish("Kiro","SaltwaterFish",10)
decoration=BaseDecoration(30,10)
base_aquarium.add_decoration(decoration)
base_aquarium.add_fish(salt_waret)
print()

