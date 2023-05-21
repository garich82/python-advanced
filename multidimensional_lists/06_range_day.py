def check_valid_pos(x, y):
    if 0 <= x < 5 and 0 <= y < 5 and matrix[x][y] == ".":
        return True


def shot_outcome(x, y):
    if x >= 5 or x < 0 or y >= 5 or y < 0:
        return "Out of range"
    elif matrix[x][y] == "x":
        return "Target hit"


matrix = [input().split() for _ in range(5)]

# Finding initial player position
player_row = -1
player_col = -1
targets_count = 0

for i in range(5):
    for j in range(5):
        if matrix[i][j] == "A":
            player_row = i
            player_col = j
            matrix[player_row][player_col] = "."
        elif matrix[i][j] == "x":
            targets_count += 1

# Directions dictionary
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

# Main logic
targets_positions = []
targets_hit = 0
n = int(input())   # Count of commands

for _ in range(n):
    command = input().split()

    if command[0] == "move":
        desired_row = player_row + directions[command[1]][0] * int(command[2])
        desired_col = player_col + directions[command[1]][1] * int(command[2])
        if check_valid_pos(desired_row, desired_col):
            player_row = desired_row
            player_col = desired_col

    else:  # Command is shoot
        bullet_row = player_row
        bullet_col = player_col
        for _ in range(5):
            shot_row = bullet_row + directions[command[1]][0]
            shot_col = bullet_col + directions[command[1]][1]
            if shot_outcome(shot_row, shot_col) == "Target hit":
                targets_hit += 1
                targets_positions.append([shot_row, shot_col])
                matrix[shot_row][shot_col] = "."
                break

            elif shot_outcome(shot_row, shot_col) == "Out of range":
                break
            else:  # Bullet continues its way
                bullet_row = shot_row
                bullet_col = shot_col

    if targets_hit == targets_count:
        print(f"Training completed! All {targets_count} targets hit.")
        break

else:
    targets_left = targets_count - targets_hit
    print(f"Training not completed! {targets_left} targets left.")

for row in targets_positions:
    print(row)
