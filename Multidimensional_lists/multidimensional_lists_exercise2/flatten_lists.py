import sys
from io import StringIO

test_case1="""1 2 3 |4 5 6 |  7  88"""
test_case2="""7 | 4  5|1 0| 2 5 |3"""
test_case3="""1| 4 5 6 7  |  8 9"""
# sys.stdin=StringIO(test_case1)
# sys.stdin=StringIO(test_case2)
# sys.stdin=StringIO(test_case3)
new_pattern=[]
pattern=input().split("|")
for idx in range(len(pattern)-1,-1,-1):
    elements=pattern[idx].split()
    new_pattern+=elements
print(" ".join(new_pattern))

