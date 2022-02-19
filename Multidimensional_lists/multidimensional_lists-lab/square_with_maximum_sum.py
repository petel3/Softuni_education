import sys
from io import StringIO

test_case1="""3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0

"""
test_case2="""2, 4
10, 11, 12, 13
14, 15, 16, 17
"""

# sys.stdin=StringIO(test_case1)
# sys.stdin=StringIO(test_case2)
row,col=[int(x)for x in input().split(", ")]
matrix=[]
max_sum=0
new_matrix=[]
for _ in range(row):
    matrix.append([int(x) for x in input().split(", ")])
for r in range(row-1):
    for c in range (col-1):
        current_sum=matrix[r][c]+\
                    matrix[r][c+1]+\
                    matrix[r+1][c]+\
                    matrix[r+1][c+1]

        if current_sum>max_sum:
            max_sum, best_row, best_col = current_sum, r, c

print(matrix[best_row][best_col], matrix[best_row][best_col+1])
print(matrix[best_row+1][best_col], matrix[best_row+1][best_col+1])
print(max_sum)
