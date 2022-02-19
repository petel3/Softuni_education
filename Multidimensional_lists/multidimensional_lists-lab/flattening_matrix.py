import sys
from io import StringIO

test_case1 = """2
1, 2, 3
4, 5, 6
"""
test_case2 = """3
10, 2, 21, 4
5, 20, 41, 9
6, 2, 4, 99
"""
# sys.stdin = StringIO(test_case1)
# sys.stdin=StringIO(test_case2)
size = int(input())
matrix = []
flattering_numbers=[]
for _ in range(size):
    matrix.append([int(x) for x in input().split(", ")])
for rows in matrix:
    for cols in rows:
        flattering_numbers.append(cols)
print(flattering_numbers)