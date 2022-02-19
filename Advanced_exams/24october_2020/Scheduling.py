from collections import deque

jobs=[int(el)for el in input().split(', ')]
idx=int(input())
elements=deque([])
result=[]
for index in range(len(jobs)) :
    elements.append([jobs[index],index])
    elements=sorted(elements)
for el in elements:
    if el[1]== idx:
        result.append(el[0])
        break
    result.append(el[0])


print(sum(result))
