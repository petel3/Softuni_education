import re
text=input()

pattern=r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)$"

list_furniture=[]
total=0
while text !="Purchase":
    furniture = re.match(pattern, text)
    if furniture is not None:
        furniture_name = furniture.group('furniture')
        list_furniture.append(furniture_name)
        price=float(furniture.group('price'))
        qty=int(furniture.group('quantity'))
        total+=price * qty

    text=input()
print("Bought furniture:")
for furniture in list_furniture:
    print(furniture)
print(f"Total money spend: {total:.2f}")