rows, cols = [int(x) for x in input().split()]
zero = 97
matrix = []

for row in range(rows):
    inner_list = []
    for col in range(cols):
        inner_list.append(chr(zero+row)+chr(zero+row+col)+chr(zero+row))
    matrix.append(inner_list)

[print(*row) for row in matrix]
