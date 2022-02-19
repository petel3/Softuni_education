r,c=[int(x) for x in input().split()]
pattern=[]
for i in range(r):

    for j in range(c):
        print(f"{chr(97+i)}{chr(97 +j+i)}{chr(97+i)}", end=" ")
    print()