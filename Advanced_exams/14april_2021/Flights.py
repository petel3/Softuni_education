def flights(*args):
    dictionary = {}
    for arg in range(len(args)):
        if args[arg]=="Finish":
            break
        if arg%2==0:
            destination=args[arg]
        else:
            passenger=int(args[arg])

            if destination not in dictionary:
                dictionary[destination]=[]
            dictionary[destination].append(passenger)

    for destination,passenger in dictionary.items():
        dictionary[destination]=sum(passenger)

    return dictionary

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))