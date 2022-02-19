string = input().split(", ")
beggars = int(input())
beggars_list = []

for x in range(0, beggars):

    temp = string[x::beggars]
    for j in range(0, len(temp)):
        temp[j] = int(temp[j])
    beggars_list.append(sum(temp))

print(beggars_list)