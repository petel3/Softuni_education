from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self,name):
        self.name = name
        self.food_menu=[]
        self.drinks_menu=[]
        self.table_repository=[]
        self.total_income=0

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value.strip()=="":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name=value

    def add_food(self,food_type,name,price):
        for food_in_menu in self.food_menu:
            if name == food_in_menu.name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        food=self.__menu_foods(food_type,name,price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self,drink_type,name,portion,brand):
        for drink_in_menu in self.drinks_menu:
            if name == drink_in_menu.name:
                raise Exception(f"{drink_type} {name} is already in the menu!")
        drink=self.__menu_drinks(drink_type,name,portion,brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self,table_type,table_number,capacity):
        for table in self.table_repository:
            if table_number == table.table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")
        table=self.__table(table_type,table_number,capacity)
        self.table_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self,number_of_people):
        for table in self.table_repository:
            if not table.is_reserved and table.capacity>=number_of_people:
                table.is_reserved=True
                table.number_of_people+=number_of_people
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
            return f"No available table for {number_of_people} people"

    def order_food(self,table_number,*food_name):
        ordered_food=[]
        not_ordered_food=[]
        for table in self.table_repository:
            if not table_number==table.table_number:
                return f"Could not find table {table_number}"
            for food in food_name:
                for food_names in self.food_menu:
                    if food in food_names.name:
                        ordered_food.append(food)
                    not_ordered_food.append(food)

            result= f"Table {table_number} ordered:\n"
            result+=f"{[repr(f)for f in ordered_food]}\n"
            result += f"{[repr(f) for f in not_ordered_food]}"

    def order_drink(self,table_number,*drink_name):
        ordered_drink = []
        not_ordered_drink = []
        for table in self.table_repository:
            if not table_number == table.table_number:
                return f"Could not find table {table_number}"
            for drink in drink_name:
                for food_names in self.food_menu:
                    if drink in drink_name.name:
                        ordered_drink.append(drink)
                    not_ordered_drink.append(drink)

            result = f"Table {table_number} ordered:\n"
            result += f"{[repr(d) for d in ordered_drink]}\n"
            result += f"{[repr(d) for d in not_ordered_drink]}"

    def leave_table(self,table_number):
        bills=0
        for table in self.table_repository:
            if table_number==table.table_number:
                bills=table.get_bill()
                table.clear()
        return f"Table: {table_number}" + "\n" + f"Bill: {bills}"


    def get_free_tables_info(self):
        return f"{[(x.free_table_info()) for x in self.table_repository if not x.is_reserved]}"


    def get_total_income(self):
        total_income=0
        for table in self.table_repository:
            total_income+=table.get_bill()
        return f"Total income: {total_income:.2f}lv"

    def __menu_foods(self,food_type,name,price):
        if food_type=="Cake":
            return Cake(name,price)
        if food_type=="Bread":
            return Bread(name,price)

    def __menu_drinks(self,drink_type,name,portion,brand):
        if drink_type=="Tea":
            return Tea(name,portion,brand)
        if drink_type=="Water":
            return Water(name,portion,brand)

    def __table(self,table_type,table_number,capacity):
        if table_type=="InsideTable":
            return InsideTable(table_number,capacity)
        if table_type=="OutsideTable":
            return OutsideTable(table_number,capacity)

    def __get_food_orders(self,name):
        foods = [f for f in self.food_menu if f.name==name]
        return foods[0] if foods else None
