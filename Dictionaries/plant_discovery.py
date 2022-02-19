n=int(input())
plant={}
for _ in range(n):
    data= input().split("<->")
    plant_name=data[0]
    rarity=int(data[1])
    if plant_name not in plant:
        plant[plant_name] = []
        plant[plant_name].append(rarity)



command=input()
while command!="Exhibition":
    data=command.split(": ")
    if data[0]=="Rate":
        cmds="".join(data[1])
        cmds=cmds.split(" - ")
        plant_name=cmds[0]
        rating=float(cmds[1])

    elif data[0]=="Update":
        cmds = "".join(data[1])
        cmds = cmds.split(" - ")
        plant_name = cmds[0]

        new_rarity=int(cmds[1])
        plant[plant_name] = new_rarity
    elif data[0]=="Reset":
        cmds = "".join(data[1])
        cmds = cmds.split(" - ")
        plant_name = cmds[0]
        if plant_name not in plant:
            print("error")
        else:
            plant[plant_name][0] = 0
    command=input()
sorted_plants=sorted(plant.items(), key=lambda tkvp: (-tkvp[1][0],-tkvp[1][1]))
print("Plants for the exhibition:")
for plant in sorted_plants:
    print(f"- {plant[0]}; Rarity: {plant[1][0]}; Rating: {plant[1][1]:.2f}")