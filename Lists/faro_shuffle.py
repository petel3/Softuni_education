cards=input().split()
shuffle=int(input())

half_length=len(cards)//2
for i in range(shuffle):

    left_side=cards[:half_length]
    right_side=cards[half_length:]
    faro_cards=[]
    for el in range(len(left_side)):
        faro_cards.append(left_side[el])
        faro_cards.append(right_side[el])
    cards=faro_cards
print(faro_cards)