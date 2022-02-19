from collections import deque


palm_firework=0
willow_firework=0
crossete_firework=0

fireworks_effect=deque([int(el) for el in input().split(", ")])
explosive_power=[int(el) for el in input().split(", ")]

while True:
    if not fireworks_effect:
        break

    if not explosive_power:
        break

    if fireworks_effect:
        effect=fireworks_effect.popleft()

    if explosive_power:
        power=explosive_power.pop()

    if effect<=0:
        explosive_power.append(power)
        continue

    if power<=0:
        fireworks_effect.appendleft(effect)
        continue

    result=effect+power
    if result%3==0 and result%5==0:
        crossete_firework+=1
    elif result%3==0:
        palm_firework+=1
    elif result%5==0:
        willow_firework+=1
    else:
        if effect>1:
            fireworks_effect.append(effect-1)
        explosive_power.append(power)


if palm_firework>=3 and crossete_firework>=3 and willow_firework>=3:
    print("Congrats! You made the perfect firework show!")
    if fireworks_effect:
        print(f"Firework Effects left: {', '.join([str(el)for el in fireworks_effect])}")
    elif explosive_power:
        print(f"Explosive Power left: {', '.join([str(el)for el in explosive_power])}")
else:
    print("Sorry. You can't make the perfect firework show.")
    if fireworks_effect:
        print(f"Firework Effects left: {', '.join([str(el) for el in fireworks_effect])}")
    elif explosive_power:
        print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossete_firework}")