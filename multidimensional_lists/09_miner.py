size = int(input())
commands = [direction for direction in input().split()]
mine = [[x for x in input().split()] for _ in range(size)]
miner_row = -1
miner_col = -1
coals = 0

for row in range(size):
    for col in range(size):
        if mine[row][col] == "s":
            miner_row, miner_col = row, col
            mine[row][col] == "*"
        elif mine[row][col] == "c":
            coals += 1

directions = {
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "down": (1, 0),

}

for i in range(len(commands)):
    desired_row = miner_row + directions[commands[i]][0]
    desired_col = miner_col + directions[commands[i]][1]
    if 0 <= desired_row < size and 0 <= desired_col < size:
        miner_row, miner_col = desired_row, desired_col
        if mine[miner_row][miner_col] == "c":
            coals -= 1
            mine[miner_row][miner_col] = "*"
            if coals == 0:
                print(f"You collected all coal! ({miner_row}, {miner_col})")
                break
        elif mine[miner_row][miner_col] == "e":
            print(f"Game over! ({miner_row}, {miner_col})")
            break
else:
    print(f"{coals} pieces of coal left. ({miner_row}, {miner_col})")

