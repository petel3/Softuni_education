import sys
from io import StringIO

test_case1="""3 4
A B B D
E B B B
I J B B
"""
test_case2="""2 2
a b
c d
"""
test_case3="""5 4
A A B D
A A B B
I J B B
C C C G
C C K P
"""
# sys.stdin=StringIO(test_case1)
# sys.stdin=StringIO(test_case2)
# sys.stdin=StringIO(test_case3)
rows,cols=[int(x) for x in input().split()]
matrix=[]
count=0
for _ in range(rows):
    matrix.append(input().split())
for r in range(rows-1):
    for c in  range(cols-1):
        if matrix[r][c] == matrix[r][c+1] == matrix[r+1][c] == matrix[r+1][c+1]:
            count+=1

print(count)

