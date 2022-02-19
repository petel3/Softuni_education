travel_stops=input()
commands=input()
while commands!="Travel":
    data=commands.split(":")
    if data[0]=="Add Stop":
        index=int(data[1])
        string=data[2]

        if index<len(travel_stops):
            travel_stops=travel_stops[:index] + string + travel_stops[index:]
        print(travel_stops)

    elif data[0]=="Remove Stop":
        start_index=int(data[1])
        end_index=int(data[2])

        if start_index<len(travel_stops) and end_index<len(travel_stops):
            left_half=travel_stops[:start_index]
            right_half=travel_stops[end_index+1:]
            travel_stops=left_half + right_half
        print(travel_stops)

    elif data[0]=="Switch":
        old_string=data[1]
        new_string=data[2]

        if old_string in travel_stops:
            travel_stops=travel_stops.replace(old_string,new_string)
        print(travel_stops)
    commands=input()
print(f"Ready for world tour! Planned stops: {travel_stops}")