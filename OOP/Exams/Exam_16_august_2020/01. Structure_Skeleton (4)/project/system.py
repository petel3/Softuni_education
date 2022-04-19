from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except:
            raise Exception("Software cannot be installed")

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except:
            raise Exception("Software cannot be installed")

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        memory_used = 0
        total_memory_used = 0
        capacity_used = 0
        total_capacity_used = 0
        for hardware in System._hardware:
            total_memory_used += hardware.memory
            total_capacity_used += hardware.capacity
            memory_used += hardware.total_memory
            capacity_used += hardware.total_capacity
        return f"System Analysis\n"\
               f"Hardware Components: {len(System._hardware)}\n"\
               f"Software Components: {len(System._software)}\n"\
               f"Total Operational Memory: {memory_used} / {total_memory_used}\n"\
               f"Total Capacity Taken: {capacity_used} / {total_capacity_used}"

    @staticmethod
    def system_split():

        result = []
        for hardware in System._hardware:
            soft_components = [s.name for s in hardware.software_components]
            info = f"Hardware Component - {hardware.name}\n" \
                   f"Express Software Components: {len([s for s in hardware.software_components if s.software_type == 'Express'])}\n" \
                   f"Light Software Components: {len([s for s in hardware.software_components if s.software_type == 'Light'])}\n" \
                   f"Memory Usage: {hardware.total_memory} / {hardware.memory}\n" \
                   f"Capacity Usage: {hardware.total_capacity} / {hardware.capacity}\n" \
                   f"Type: {hardware.hardware_type}\n" \
                   f"Software Components: {', '.join(soft_components) if soft_components else None}"

            result.append(info)

        return '\n'.join(result).strip()
