n=int(input())
pianist={}
for _ in range(n):
    data=input().split("|")
    piece=data[0]
    composer=data[1]
    key=data[2]
    pianist[piece]={"Composer":composer,"Key":key}
command=input()
while command!="Stop":
    data=command.split("|")
    if data[0]=="Add":
        piece = data[1]
        composer = data[2]
        key = data[3]
        if piece in pianist:
            print(f"{piece} is already in the collection!")
        else:
            pianist[piece] = {"Composer": composer, "Key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif data[0]=="Remove":
        piece=data[1]
        if piece not in pianist:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del pianist[piece]
            print(f"Successfully removed {piece}!")
    elif data[0]=="ChangeKey":
        piece=data[1]
        new_key=data[2]
        if piece not in pianist:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pianist[piece]["Key"]=new_key
            print(f"Changed the key of {piece} to {new_key}!")

    command=input()
sorted_pianist=sorted(pianist.items(), key=lambda tkvp: (tkvp[0],tkvp[1]["Composer"]))
for pianist in sorted_pianist:
    print(f"{pianist[0]} -> Composer: {pianist[1]['Composer']}, Key: {pianist[1]['Key']}")