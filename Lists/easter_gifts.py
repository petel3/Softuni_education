gifts=input().split()

command=input()
while  command!="No Money":
    command=command.split()

    if  "OutOfStock" in command:
        gift = command[1]

        while gift in gifts:
            gifts[gifts.index(gift)]= "None"

    elif "Required" in command:
        gift = command[1]
        gift_index=int(command[2])

        if 0<=gift_index<len(gifts):
            gifts[gift_index]=gift

    elif "JustInCase" in command:
        gift = command[1]
        gifts[-1]=gift
    command=input()

gifts = [g for g in gifts if g != "None"]
print(*gifts)