import sys
from io import StringIO

test_case1="""3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
"""

def is_valid_matrix(r,c,size):
    return 0<=r<size and 0<=c<size

# sys.stdin=StringIO(test_case1)
size=int(input())
matrix=[]
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command=input()
    if command=="END":
        break
    args=command.split()
    r=int(args[1])
    c=int(args[2])
    number=int(args[3])
    if is_valid_matrix(r,c,size):

        if args[0]=="Add":
            matrix[r][c]+=number
        elif args[0]=="Subtract":
            matrix[r][c] -= number
    else:
        print("Invalid coordinates")
for r in matrix:
    print(" ".join([str(x)for x in r]))


