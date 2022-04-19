class Child:
    def __init__(self,food_cost: int, *toys_cost):
        self.cost=sum(toys_cost) + food_cost
