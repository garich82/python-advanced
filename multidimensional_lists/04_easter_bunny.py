def is_valid_index(x, y):
    if 0 <= x < size and 0 <= y < size:
        return True


size = int(input())
matrix = [[int(x) if x not in ["X","B"] else x for x in input().split()] for _ in range(size)]
eggs_positions = []
best_direction = None
max_sum_eggs = float("-inf")
bunny_pos = []

directions = {
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
    "up": (-1, 0),
}

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "B":
            bunny_pos = [row, col]


for direction in ["right", "down", "left", "up"]:
    current_eggs_positions = []
    current_sum_eggs = 0
    new_row = bunny_pos[0]
    new_col = bunny_pos[1]

    while True:
        new_row += directions[direction][0]
        new_col += directions[direction][1]
        if is_valid_index(new_row, new_col):
            if matrix[new_row][new_col] == "X":
                break
            else:
                current_sum_eggs += matrix[new_row][new_col]
                current_eggs_positions.append([new_row, new_col])
        else:
            break

    if current_sum_eggs > max_sum_eggs:
        max_sum_eggs = current_sum_eggs
        eggs_positions = current_eggs_positions
        best_direction = direction

print(best_direction)
print(*eggs_positions, sep="\n")
print(max_sum_eggs)
