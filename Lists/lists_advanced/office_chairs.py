n=int(input())
left_chairs = 0
counter=0
for room in range(n):
    chairs = input().split()
    chair, visitor = chairs[0], chairs[1]
    if int(visitor) > len(chair):
        result=int(visitor)-len(chair)
        print(f'{result} more chairs needed in room {room+1}')
        counter=+1
    elif int(visitor)<len(chair):
        result = len(chair) - int(visitor)
        left_chairs += result
if counter==0:
    print(f"Game On, {left_chairs} free chairs left")



