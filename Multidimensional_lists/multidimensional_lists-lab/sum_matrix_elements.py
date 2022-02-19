import sys
from io import StringIO

test_case1="""3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
"""
# sys.stdin=StringIO(test_case1)



r,c = [int(x) for x in input().split(", ")]
matrix=[]
result=0
for _ in range (r):
    matrix.append([int(x)for x in input().split(", ")])
for rows in matrix:
    for cols in rows:
        result+=cols

print(result)
print(matrix)


