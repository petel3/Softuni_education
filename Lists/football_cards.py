teamA=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
teamB=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
is_terminated=False
card=input().split()

for cards in card:
    cartons=cards.split("-")
    team_name=cartons[0]
    player=int(cartons[1])

    if team_name== "A" and player in teamA:
        teamA.remove(player)
    elif  team_name== "B" and player in teamB:
        teamB.remove(player)

    if len(teamA)<7 or len(teamB)<7:
        is_terminated=True
        break

print(f"Team A - {len(teamA)}; Team B - {len(teamB)}")
if is_terminated:
    print("Game was terminated")
