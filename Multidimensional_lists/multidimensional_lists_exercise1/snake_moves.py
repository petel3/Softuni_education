import sys
from io import StringIO

test_case1="""5 6
SoftUni
"""
# sys.stdin=StringIO(test_case1)
rows,cols=[int(x) for x in input().split()]
word=input()
matrix=[]
word_idx=0
for row in range(rows):
    matrix.append([None]*cols)
    for col in range(cols):
        if row%2==0:
            matrix[row][col]=word[word_idx]

        else:
            matrix[row][cols-col-1]=word[word_idx]

        word_idx=(word_idx+1)%(len(word))
[print(''.join(x)) for x in matrix]