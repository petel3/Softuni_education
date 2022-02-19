def is_in_range(row,col,size):
    if 0<=row<size and 0<=col<size:
        return True
    return False

def get_turn():
    turn_string=input()
    vals=turn_string[1:-1].split(", ")
    return [int(val) for val in vals]

def get_value(board,row_index,col_index):

    if not is_in_range(row_index,col_index,size):
        return 0
    target=board[row_index][col_index]
    if target.isdigit():
        return int(target)

    value=int(board[row_index][0])+int(board[row_index][-1])+ \
          int(board[0][col_index])+int(board[-1][col_index])
    if target=="T":
        return value*3
    elif target=="D":
        return value*2
    return 501

def solve(board,player_names,size):
    current_player=player_names[0],501,0
    other_player=player_names[1],501,0

    while True:
        name, total_points, turns = current_player
        (row_index,col_index)=get_turn()




        current_points=get_value(board,row_index,col_index)
        total_points -= current_points
        turns+=1

        current_player=(name,total_points,turns)

        if total_points<=0:
            break

        current_player, other_player = other_player, current_player
    (name, _, turns) = current_player

    print(f'{name} won the game with {turns} throws!')

size=7
player_names=input().split(", ")

board=[]

for _ in range(size):
    board.append([el for el in input().split(" ")])


solve(board,player_names,size)

