import sys
from io import StringIO

test_case1="""3
ABC
DEF
X!@
!
"""
test_case2="""4
asdd
xczc
qwee
qefw
4
"""
# sys.stdin=StringIO(test_case1)
# sys.stdin=StringIO(test_case2)
size=int(input())
matrix=[]
symbol=[]
is_found=False

for _ in range(size):
    matrix.append([x for x in input()])
symbol_to_find=input()
for r in range(len(matrix)):
    if is_found:
        break
    for c in range(len(matrix)):
        if symbol_to_find in matrix[r][c]:
            symbol=r,c
            is_found=True
            break
if is_found:
    print(symbol)

else:
    print(f"{symbol_to_find} does not occur in the matrix")