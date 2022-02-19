def is_in_range(row,col,size):
    if 0<=row<size and 0<=col<size:
        return True
    return False

def get_next_position(command,row,col):
    if command=="up":
        return row-1,col
    elif command=="down":
        return row+1,col
    elif command=="left":
        return row,col-1
    elif command=="right":
        return row,col+1

initial_string=input()
size=int(input())
matrix=[]
current_row,current_col=0,0

for _ in range(size):
    matrix.append([el for el in input()])

for row in range(size):
    for col in range(size):
        if matrix[row][col]=="P":
            current_row,current_col=row,col
n=int(input())

for _ in range(n):
    command=input()
    next_row,next_col=get_next_position(command,current_row,current_col)

    if is_in_range(next_row,next_col,size):

        if matrix[next_row][next_col]!="-":
            initial_string+=(matrix[next_row][next_col])

        matrix[next_row][next_col]="P"
        matrix[current_row][current_col]="-"
        current_row,current_col=next_row,next_col

    else:
        initial_string=initial_string[:-1]
        break

print(initial_string)
for row in range(size):
    print(''.join(matrix[row]))

