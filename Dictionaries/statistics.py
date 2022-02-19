commands=input()
products={}

while not commands=="statistics":
    data=commands.split(": ")
    if data[0] not in products:
        product=data[0]
        value=int(data[1])
        products[product]=value
    else:
        product = data[0]
        value = int(data[1])
        products[product] += value
    commands=input()
print("Products in stock:")
for key,value in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")