def is_in_range(row,col,size):
    if 0<=row<size and 0<=col<size:
        return True
    return False



directions={
    "up":(-1,0),
    "down":(1,0),
    "left":(0,-1),
    "right":(0,1),
    "left_up":(-1,-1),
    "left_down":(+ 1,-1),
    "right_up":(-1,+1),
    "right_down":(+ 1,+1)
}
board=[]
size=8
king_row,king_col=0,0
queens=[]
for _ in range(size):
    board.append(input().split())
for row in range(size):
    for col in range(size):
        if board[row][col]=="Q":
            for direction in directions:
                next_row=row+directions[direction][0]
                next_col = col+ directions[direction][1]
                while is_in_range(next_row,next_col,size):
                    if board[next_row][next_col] == "Q":
                        break
                    if board[next_row][next_col]=="K":
                        queens.append([row,col])
                        break
                    next_row += directions[direction][0]
                    next_col += directions[direction][1]

if queens:
    for queen in queens:
        print(queen)
else:
    print("The king is safe!")
