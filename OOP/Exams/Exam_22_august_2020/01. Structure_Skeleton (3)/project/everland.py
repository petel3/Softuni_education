from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.expenses + room.room_cost
        return f"Monthly consumption: {result:.2f}$."

    def pay(self):
        pay=[]
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                room.budget-= room.expenses+room.room_cost
                pay.append(f"{room.family_name} paid {room.expenses+room.room_cost:.2f}$ and have {room.budget}$ left.")
            else:

                self.rooms.remove(room)
                pay.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
        return "\n".join(pay)
    def status(self):
        all_members = sum([r.members_count for r in self.rooms])
        info = [f"Total population: {all_members}"]
        for room in self.rooms:

            info.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if room.children:
                count=0
                for child in room.children:
                    count+=1
                    info.append(f"--- Child {count} monthly cost: {child.cost*30:.2f}$")
            info.append(f"--- Appliances monthly cost: {room.expenses:.2f}$")



        return "\n".join(info)
