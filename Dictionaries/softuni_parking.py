n=int(input())
parking={}
for _ in range (n):
    data=input().split()

    if data[0]=="register":
        user, license_plate_number = data[1], data[2]
        if user not in parking:
            parking[user]=license_plate_number
            print(f"{user} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif data[0]=="unregister":
        user=data[1]
        if user not in parking:
            print(f"ERROR: user {user} not found")
        else:
            parking.pop(user)
            print(f"{user} unregistered successfully")

for user,license_plate_number in parking.items():
    print(f"{user} => {license_plate_number}")