def is_in_range(row,col,size):
    if 0<=row<size and 0<=col<size:
        return True
    return False

def is_it_bomb(matrix,row,col):
    result=0
#up
    if is_in_range(row-1,col,size) and matrix[row-1][col]==bomb:
        result+=1
#down
    if is_in_range(row+1,col,size) and matrix[row+1][col]==bomb:
        result+=1
#left
    if is_in_range(row,col-1,size)and matrix[row][col-1]==bomb:
        result+=1
#right
    if is_in_range(row,col+1,size) and matrix[row][col+1]==bomb:
        result+=1
#up_left
    if is_in_range( row + 1, col -1,size)and matrix[row+1][col-1]==bomb:
        result += 1
#up_right
    if is_in_range( row - 1, col + 1,size) and matrix[row-1][col+1]==bomb:
        result += 1
#down_left
    if is_in_range( row - 1, col -1,size) and matrix[row-1][col-1]==bomb:
        result += 1
#down_right
    if is_in_range(row + 1, col + 1,size) and matrix[row+1][col+1]==bomb:
        result += 1

    return result

size=int(input())
matrix=[]
bomb="*"
r_mine,c_mine=0,0

for row in range(size):
    matrix.append([0]*size)
n=int(input())

for _ in range(n):
    coordinates=input()
    coordinates=coordinates[1:-1]
    r_mine,c_mine=int(coordinates.split(', ')[0]), int(coordinates.split(', ')[1])

    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if r==r_mine and c==c_mine:
                matrix[r][c]=bomb

while True:
    for r in range(len(matrix)):
        for c in range(len(matrix)):

            if not matrix[r][c]==bomb:
                matrix[r][c]=is_it_bomb(matrix,r,c)
            else:
                continue
    break
for row in matrix:
    print(' '.join(str(el)for el in row))

