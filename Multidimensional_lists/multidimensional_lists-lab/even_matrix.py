import sys
from io import StringIO

test_case1="""2
1, 2, 3
4, 5, 6
"""
test_case2="""4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67
"""
# sys.stdin=StringIO(test_case1)
# sys.stdin=StringIO(test_case2)
size = int(input())
matrix=[]
even_matrix=[]
for _ in range (size):
    matrix.append([int(x)for x in input().split(", ")])
for rows in matrix:
    even_matrix.append([int(el) for el in rows if int(el)%2==0])
print(even_matrix)
