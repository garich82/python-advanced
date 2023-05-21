from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = deque(input())
snake_copy = snake.copy()
matrix = []

for i in range(rows):
    inner_list = list([0] * cols)
    matrix.append(inner_list)

for row_index in range(rows):
    if row_index % 2 == 0:
        col_range = range(0, cols)
    else:
        col_range = range(cols - 1, -1, -1)

    for col_index in col_range:
        if not snake_copy:
            snake_copy = snake.copy()
        matrix[row_index][col_index] = snake_copy.popleft()

[print(*row, sep="") for row in matrix]
