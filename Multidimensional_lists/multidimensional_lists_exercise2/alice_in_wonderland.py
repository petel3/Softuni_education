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

size=int(input())
matrix=[]
tea_bags=0
current_row,current_col=0,0

for _ in range(size):
    matrix.append([el for el in input().split()])

for row in range(size):
    for col in range(size):
        if matrix[row][col]=="A":
            matrix[row][col]="*"
            current_row,current_col=row,col

while True:
    value=''
    commands= input()
    current_row,current_col=get_next_position(commands,current_row,current_col)
    if not is_in_range(current_row,current_col,size) :
        break
    value=matrix[current_row][current_col]
    matrix[current_row][current_col] = "*"


    if value.isdigit():
        tea_bags+=int(value)
    if value=="R" or tea_bags>=10:
        break


if tea_bags>=10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(' '.join(row))
