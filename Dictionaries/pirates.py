start_commands=input()
cities_dict={}

while start_commands !="Sail":
    data=start_commands.split("||")
    city=data[0]
    population=int(data[1])
    gold = int(data[2])
    if city in cities_dict:
        cities_dict[city]['population']+=population
        cities_dict[city]['gold'] += gold

    else:
        cities_dict[city]={'population':population,'gold':gold}

    start_commands=input()
end_command=input()
while end_command !="End":

    cmds=end_command.split("=>")
    command=cmds[0]

    if command == "Plunder":
        city=cmds[1]
        people=int(cmds[2])
        gold=int(cmds[3])
        cities_dict[city]['population'] -= people
        cities_dict[city]['gold'] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities_dict[city]['population']<=0 or cities_dict[city]['gold']<=0:
             del cities_dict[city]
             print(f"{city} has been wiped off the map!")
    elif command=="Prosper":
        city=cmds[1]
        gold=int(cmds[2])
        if gold<0:
            print("Gold added cannot be a negative number!")
        else:
            cities_dict[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities_dict[city]['gold']} gold.")

    end_command=input()
if not cities_dict:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
sorted_result= sorted(cities_dict.items(),key=lambda kvp: (-kvp[1]['gold'], kvp[0]))
for cities_dict in sorted_result:
    print(f"{cities_dict[0]} -> Population: {cities_dict[1]['population']} citizens, Gold: {cities_dict[1]['gold']} kg")