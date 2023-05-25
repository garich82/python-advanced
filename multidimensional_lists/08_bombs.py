def is_valid_index(x, y):
    if 0 <= x < size and 0 <= y < size and matrix[x][y] > 0:
        return True


size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
bombs = [[int(x) for x in y.split(',')] for y in input().split()]

directions = [
    [-1, -1],   # Up left
    [-1, 0],    # Up
    [-1, 1],    # Up right
    [0, 1],     # Right
    [1, 1],     # Down right
    [1, 0],     # Down
    [1, -1],    # Down left
    [0, -1]     # Left
]

for i in range(len(bombs)):
    bomb_x, bomb_y = bombs[i]
    bomb_power = matrix[bomb_x][bomb_y]
    if bomb_power > 0:
        for direction in directions:
            explosion_x = bomb_x + direction[0]
            explosion_y = bomb_y + direction[1]
            if is_valid_index(explosion_x, explosion_y):
                matrix[explosion_x][explosion_y] -= bomb_power
        matrix[bomb_x][bomb_y] = 0

count_live_cells = 0
sum_live_cells = 0

for i in range(size):
    for j in range(size):
        if matrix[i][j] > 0:
            count_live_cells += 1
            sum_live_cells += matrix[i][j]

print(f"Alive cells: {count_live_cells}")
print(f"Sum: {sum_live_cells}")
[print(*row) for row in matrix]

