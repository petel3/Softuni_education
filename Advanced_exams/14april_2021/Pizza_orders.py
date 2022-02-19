from collections import deque
pizza_counter=0
pizza_orders=deque([int(el) for el in input().split(", ")])
employees=[int(el) for el in input().split(", ")]
while True:
    if not pizza_orders:
        break
    if not employees:
        break
    order=pizza_orders.popleft()
    get_order_from_employees=employees.pop()
    if order>10 or order<=0:
        employees.append(get_order_from_employees)
        continue

    elif order<=get_order_from_employees:

        pizza_counter+=order


    elif order>get_order_from_employees:
        pizza_counter+=get_order_from_employees
        pizza_orders.appendleft(order-get_order_from_employees)

        continue
if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el)for el in pizza_orders])}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizza_counter}")
    print(f"Employees: {', '.join([str(el)for el in employees])}")
