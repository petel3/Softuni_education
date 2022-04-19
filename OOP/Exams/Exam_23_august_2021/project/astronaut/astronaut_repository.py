from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts=[]

    def add(self,astronaut:Astronaut):
        self.astronauts.append(astronaut)

    def remove(self,astronaut:Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self,name):
        for astronaut in self.astronauts:
            if name == astronaut.name:
                return astronaut
        return None

    def prepare_austronauts_for_mission(self,count,min_oxygen):
        result=sorted([x for x in self.astronauts if x.oxygen>min_oxygen], key=lambda x:x.oxygen, reverse=True)[0:count]
        return result