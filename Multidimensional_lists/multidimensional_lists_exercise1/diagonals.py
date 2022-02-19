import sys
from io import StringIO

test_case1="""3
1, 2, 3
4, 5, 6
7, 8, 9
"""
# sys.stdin=StringIO(test_case1)
size=int(input())
matrix=[]

primary_diagonal=[]
secondary_diagonal=[]

for _ in range(size):
    matrix.append([int(x) for x in input().split(", ")])

for r in range(len(matrix)):
    primary_diagonal.append(matrix[r][r])
    secondary_diagonal.append(matrix[r][size-1-r])

primady_diagonal_sum=sum(primary_diagonal)
secondary_diagonal_sum=sum(secondary_diagonal)

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {primady_diagonal_sum}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {secondary_diagonal_sum}")