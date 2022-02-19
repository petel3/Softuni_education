def is_in_range(row,col,size):
    if 0<=row<size and 0<=col<size:
        return True
    return False

size=int(input())
matrix=[]
directions={
    "up":(-1,0),
    "down":(1,0),
    "left":(0,-1),
    "right":(0,1)
}

best_direction=''
bunny_row,bunny_col=0,0
max_eggs=0
bunny=[]
best_path=[]

for _ in range(size):
    matrix.append([el for el in input().split()])

for row in range(size):
    for col in range(size):
        if matrix[row][col]=="B":
            bunny_row,bunny_col=row,col

for direction in directions:
    eggs=0
    current_row,current_col=bunny_row,bunny_col
    bunny = []

    while True:
        current_row=current_row+directions[direction][0]
        current_col=current_col+directions[direction][1]

        if not is_in_range(current_row, current_col, size):
            break
        if matrix[current_row][current_col]=="X":
            break
        if matrix[current_row][current_col]!="B":
            eggs+=int(matrix[current_row][current_col])
            bunny.append([current_row,current_col])

    if eggs>=max_eggs:
        max_eggs=eggs
        best_direction=direction
        best_path=bunny

print(best_direction)
for path in best_path:
    print(path)
print(max_eggs)





