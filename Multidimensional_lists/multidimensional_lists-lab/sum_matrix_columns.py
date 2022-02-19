import sys
from io import StringIO

test_case1="""3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
"""
test_case2="""3, 3
1 2 3
4 5 6
7 8 9
"""
# sys.stdin=StringIO(test_case1)
# sys.stdin=StringIO(test_case2)
r,c = [int(x) for x in input().split(", ")]
matrix=[]
result=0
for _ in range(r):
    matrix.append([int(x)for x in input().split()])
n=len(matrix)
m=len(matrix[0])
column_sum=[0]*m

for r in range(n):
    for c in range(m):
        result=matrix[r][c]
        column_sum[c]+=result
[print(x) for x in column_sum]


