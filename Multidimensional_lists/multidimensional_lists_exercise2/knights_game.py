size=int(input())
board=[]
r=0
c=0
def is_knight_placed(board,row,col):
    board_size=len(board)
    if 0>row or row>=board_size or 0>col or col>=board_size:
        return False
    return board[row][col]=="K"


def count_affected_knights(board,row,col):
    result=0

    if is_knight_placed(board,row-2,col-1):
        result+=1
    if is_knight_placed(board,row-2,col+1):
        result+=1
    if is_knight_placed(board,row+2,col-1):
        result+=1
    if is_knight_placed(board,row+2,col+1):
        result+=1
    if is_knight_placed(board, row - 1, col -2):
        result += 1
    if is_knight_placed(board, row - 1, col + 2):
        result += 1
    if is_knight_placed(board, row + 1, col -2):
        result += 1
    if is_knight_placed(board, row + 1, col + 2):
        result += 1

    return result

counter_of_removed_knights=0

for _ in range(size):
    board.append(list(input()))
while True:
    max_count,knight_row,knight_col=0,0,0
    for r in range(size):
        for c in range(size):
            if board[r][c]=="0":
                continue
            count= count_affected_knights(board,r,c)
            if count>max_count:
                max_count,knight_row,knight_col=count,r,c
    if max_count==0:
        break
    board[knight_row][knight_col]="0"
    counter_of_removed_knights+=1
print(counter_of_removed_knights)