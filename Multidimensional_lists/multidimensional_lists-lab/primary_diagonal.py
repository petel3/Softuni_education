import sys
from io import StringIO

test_case1="""3
11 2 4
4 5 6
10 8 -12
"""
test_case2="""3
1 2 3
4 5 6
7 8 9
"""
# sys.stdin=StringIO(test_case1)
# sys.stdin=StringIO(test_case2)
size=int(input())
matrix=[]
result=0
for _ in range(size):
    matrix.append([int(x)for x in input().split()])
for r in range (len(matrix)):
    result+=(matrix[r][r])
print(result)
