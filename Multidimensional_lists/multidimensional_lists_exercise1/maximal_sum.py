import sys
from io import StringIO

test_case1="""4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4
"""
test_case2="""5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5
"""
sys.stdin=StringIO(test_case1)
# sys.stdin=StringIO(test_case2)

row,col=[int(x)for x in input().split()]
matrix=[]
max_sum=0
new_matrix=[]
for _ in range(row):
    matrix.append([int(x) for x in input().split()])
for r in range(row-2):
    for c in range (col-2):
        current_sum=matrix[r][c]+\
                    matrix[r][c+1]+ \
                    matrix[r][c + 2] + \
                    matrix[r+1][c]+\
                    matrix[r+1][c+1]+\
                    matrix[r + 1][c + 2]+ \
                    matrix[r + 2][c] + \
                    matrix[r + 2][c + 1] + \
                    matrix[r + 2][c + 2]

        if current_sum>=max_sum:
            max_sum, best_row, best_col = current_sum, r, c
print(f"Sum = {max_sum}")
print(matrix[best_row][best_col], matrix[best_row][best_col+1], matrix[best_row][best_col+2])
print(matrix[best_row+1][best_col], matrix[best_row+1][best_col+1], matrix[best_row+1][best_col+2])
print(matrix[best_row+2][best_col], matrix[best_row+2][best_col+1], matrix[best_row+2][best_col+2])