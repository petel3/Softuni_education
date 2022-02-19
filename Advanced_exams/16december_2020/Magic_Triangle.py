def get_magic_triangle(n):
    triangle=[[1],[1,1]]
    for row in range(2,n):
        triangle.append([])
        triangle[-1].append(1)
        for col in range(1,row):
            left=triangle[row-1][col-1]
            right=triangle[row-1][col]
            triangle[-1].append(left+right)
        triangle[-1].append(1)
    return triangle

print(get_magic_triangle(5))