def is_in_range(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False
current_rows,current_cols=0,0
presents=int(input())
initial_presents=presents
size=int(input())
good_kids=0
def get_direction(command, row, col):
    if command == "up":
        return row - 1, col
    if command == "down":
        return row + 1, col
    if command == "left":
        return row, col - 1
    return row, col + 1

def get_houses_in_range(size,row,col):
    houses=[]
    if is_in_range(row - 1,col,size):
        houses.append([row - 1, col])
    if is_in_range(row + 1, col,size):
        houses.append([row+1,col])
    if is_in_range(row, col - 1,size):
        houses.append([row,col-1])
    if is_in_range(row, col + 1,size):
        houses.append([row,col+1])
    return houses

matrix=[]
for _ in range(size):
    matrix.append([el for el in input().split()])

for rows in range(size):
    for cols in range(size):
        if matrix[rows][cols]=="S":
            current_rows,current_cols=rows,cols
        elif matrix[rows][cols]=="V":
            good_kids+=1
initial_good_kids=good_kids
while True:
    command=input()
    if command=="Christmas morning":
        break

    next_row,next_col=get_direction(command,current_rows,current_cols)
    if is_in_range(next_row, next_col, size):
        matrix[current_rows][current_cols] = "-"
        if matrix[next_row][next_col] == "V":
            good_kids-=1
            presents -= 1
            current_rows, current_cols = next_row, next_col
            matrix[current_rows][current_cols] = "S"
        elif matrix[next_row][next_col] == "X" or matrix[next_row][next_col] == "-" :
            current_rows, current_cols = next_row, next_col
            matrix[current_rows][current_cols] = "S"
            continue
        elif matrix[next_row][next_col] == "C":

            matrix[next_row][next_col] = "S"
            houses_in_range = get_houses_in_range(size,next_row, next_col, )
            for r, c in houses_in_range:
                if matrix[r][c] == "X":
                    presents -= 1
                    matrix[r][c] = "-"
                if matrix[r][c] == "V":
                    presents-=1
                    good_kids-=1
                    matrix[r][c] = "-"
                if presents==0:
                    break
    if presents==0:
        break


if  presents==0 and good_kids>0:
    print("Santa ran out of presents!")

for row in matrix:
    print(" ".join(row))

if good_kids<=0:
    print(f"Good job, Santa! {initial_good_kids} happy nice kid/s.")

else:
    print(f"No presents for {good_kids} nice kid/s.")
