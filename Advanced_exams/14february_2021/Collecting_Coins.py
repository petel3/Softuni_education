def is_in_range(row,col,size):
    if 0<=row<size and 0<=col<size:
        return True
    return False

size=int(input())
matrix=[]
coins=0
path=[]
def get_next_position(command,row,col):
    if command=="up":
        return row-1,col
    elif command=="down":
        return row+1,col
    elif command=="left":
        return row,col-1
    elif command=="right":
        return row,col+1

current_row, next_col= 0,0
player_row,player_col=0,0
for _ in range(size):
    matrix.append([el for el in input().split()])

for row in range(size):
    for col in range(size):
        if matrix[row][col]=="P":
            player_row,player_col=row,col


while True:
    command=input()
    if not command:
        break
    player_row,player_col=get_next_position(command,player_row,player_col)

    if not is_in_range(player_row,player_col, size) or matrix[player_row][player_col]== "X":
        coins=coins//2
        break
    else:
      coins+=int(matrix[player_row][player_col])

      path.append([player_row,player_col])
    if  coins>=100:
        break
if coins>=100:
    print(f"You won! You've collected {coins} coins.")
    print("Your path:")
    [print(el) for el in path]
else:
    print(f"Game over! You've collected {coins} coins.")
    print("Your path:")
    [print(el) for el in path]


