from collections import deque
customers=deque([int(el) for el in input().split(", ")])
taxis=[int(el) for el in input().split(", ")]
time=0
customer,taxi=0,0

while True:

    customer=customers.popleft()
    if taxis:
        taxi=taxis.pop()
    else:
        customers.appendleft(customer)
        break
    if taxi<customer:
        customers.appendleft(customer)
    else:
        time+=customer

    if not customers:
        break
if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {time} minutes")
elif not taxis:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(el)for el in customers])}")
