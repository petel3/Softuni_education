fires=input().split("#")
water=int(input())
efforts=0
fire_level=0
valid_fires=[]
is_water_gone=False
for fire in fires:
    fire_info=fire.split("=")
    type_fire=fire_info[0]
    range=int(fire_info[1])

    if water < int(range):
        continue

    if "High" in type_fire and int(range) <=125 and int(range)>=81:
        fire_level+=range
        water -= int(range)
        efforts += int(range) * 0.25

    elif "Medium" in type_fire and int(range) <=80 and int(range)>=51:
        fire_level+=range
        water -= int(range)
        efforts += int(range) * 0.25

    elif "Low" in type_fire and int(range) <=50 and int(range)>=1:
        fire_level+=range
        water -= int(range)
        efforts += int(range) * 0.25

    else:
        is_water_gone=True
        continue
    valid_fires.append(range)

print("Cells:")
if is_water_gone:
    for valid in valid_fires:
        print(f" - {valid}")
else:
    for fire in fires:

        fire_info = fire.split("=")
        print(f" -{fire_info[1]}")

print(f"Effort: {efforts:.2f}")
print(f"Total Fire: {fire_level}")

