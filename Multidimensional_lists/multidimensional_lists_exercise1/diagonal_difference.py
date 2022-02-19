import sys
from io import StringIO

test_case1="""3
11 2 4
4 5 6
10 8 -12
"""
test_case2="""4
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14

"""
# sys.stdin=StringIO(test_case1)
# sys.stdin=StringIO(test_case2)
size=int(input())
matrix=[]

first_diagonal_sum=[]
secondary_diagonal_sym=[]

for _ in range(size):
    matrix.append([int(x) for x in input().split()])
for r in range (len(matrix)):
    first_diagonal_sum.append(matrix[r][r])
    secondary_diagonal_sym.append(matrix[r][size-1-r])
print(abs(sum(first_diagonal_sum)- (sum(secondary_diagonal_sym))))
