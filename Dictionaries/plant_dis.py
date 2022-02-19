plants = {}

num = int(input())

for i in range(num):
    command = input().split("<->")
    flower = command[0]
    rarity = int(command[1])
    if flower not in plants:
        plants[flower] = []
        plants[flower].append(rarity)

while True:
    another_command = input().split(": ")
    action = another_command[0]
    if action == "Exhibition":
        break
    if action == "Rate":
        another_command[1] = another_command[1].split(" - ")
        flower = another_command[1][0]
        if flower not in plants:
            print("error")
        else:
            plants[flower].append(int(another_command[1][1]))
    elif action == "Update":
        another_command[1] = another_command[1].split(" - ")
        flower = another_command[1][0]
        if flower not in plants:
            print("error")
        else:
            plants[flower][0] = int(another_command[1][1])
    elif action == "Reset":
        flower = another_command[1]
        if flower not in plants:
            print("error")
        else:
            plants[flower] = [plants[flower][0]]
print("Plants for the exhibition:")
for key, value in plants.items():
    for el in value:
        total = 0
        if len(value) == 1:
            plants[key].append(0)
            break
        else:
            for el in value[1:]:
                total += el
            total /= len(value[1:])
            plants[key] = [plants[key][0]]
            plants[key].append(total)
            break
plants = dict(sorted(plants.items(), key=lambda x: (-x[1][0], -x[1][1])))
for el, v in plants.items():
    print(f"- {el}; Rarity: {v[0]}; Rating: {v[1]:.2f}")
