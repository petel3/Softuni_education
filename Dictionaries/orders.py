orders = {}
data = input()
while not data == "buy":
    product, price, quantity = data.split()
    price =float(price)
    quantity=int(quantity)
    if product not in orders:
        orders[product] = {'price':price, 'quantity':quantity}
        data=input()
        continue
    orders[product]['price']=price
    orders[product]['quantity']+=quantity
    data = input()
orders={p: i['price']*i ['quantity'] for p,i in orders.items()}
for p, i in orders.items():
    print(f"{p} -> {i:.2f}")