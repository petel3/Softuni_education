import sys
from io import StringIO

test_case1="""2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
"""
test_case2="""1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END
"""



# sys.stdin=StringIO(test_case1)
# sys.stdin=StringIO(test_case2)
def is_valid_matrix(r,c,rows,cols):
    return 0<=r<rows and 0<=c<cols
rows,cols =[int(x) for x in input().split()]
matrix=[]
for _ in range(rows):
    matrix.append([x for  x in input().split()])


while True:
    command=input()
    if command=="END":
        break
    args=command.split()
    if  args[0] !="swap" or len(args)!=5:
        print("Invalid input!")
        continue
    r1,c1,r2,c2=[int(x) for x in args[1:]]

    if not is_valid_matrix(r1,c1,rows,cols) or not is_valid_matrix(r2,c2,rows,cols):
        print("Invalid input!")
        continue
    matrix[r1][c1],matrix[r2][c2]=matrix[r2][c2],matrix[r1][c1]

    for row_elements in matrix:
        print(" ".join([str(x) for x in row_elements]))






