from collections import deque
matches_count=0
males=[int(el) for el in input().split() if int(el)>0]
females=deque([int(el) for el in input().split() if int(el)>0])
while males and females:
    if males[-1] % 25 == 0 or females[0] % 25 == 0:
        if males[-1] % 25 == 0:
            males.pop()

        if females[0] % 25 == 0:
            females.popleft()
    else:
        male = males.pop()
        female=females.popleft()


        if male==female:
            matches_count+=1
        else:
            if (male-2)>0:
                males.append(male-2)

print(f"Matches: {matches_count}")
if males:
    print(f"Males left: {', '.join([str(el)for el in males[::-1]])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print("Females left: none")

