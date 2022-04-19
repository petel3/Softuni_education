

from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.total_memory = 0
        self.total_capacity = 0
        self.software_components = []

    def install(self, software: Software):
        if software.capacity_consumption <= self.available_capacity and \
                software.memory_consumption <= self.available_memory:
            self.total_capacity += software.capacity_consumption
            self.total_memory += software.memory_consumption
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.total_capacity -= software.capacity_consumption
            self.total_memory -= software.memory_consumption
            self.software_components.remove(software)

    @property
    def available_memory(self):
        return self.memory - sum([s.memory_consumption for s in self.software_components])

    @property
    def available_capacity(self):
        return self.capacity - sum([s.capacity_consumption for s in self.software_components])
