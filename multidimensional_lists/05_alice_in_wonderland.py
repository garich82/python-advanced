size = int(input())

matrix = []
for _ in range(size):
    row = input().split()
    matrix.append(row)

alice_row = -1
alice_col = -1
for i in range(size):
    for j in range(size):
        if matrix[i][j] == "A":
            alice_row = i
            alice_col = j
            matrix[alice_row][alice_col] = "*"
            break
    if alice_row != -1:
        break

tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    alice_row += directions[command][0]
    alice_col += directions[command][1]

    if alice_row < 0 or alice_row >= size or alice_col < 0 or alice_col >= size:
        print("Alice didn't make it to the tea party.")
        break
    elif matrix[alice_row][alice_col] == "R":
        print("Alice didn't make it to the tea party.")
        matrix[alice_row][alice_col] = "*"
        break
    elif matrix[alice_row][alice_col].isdigit():
        tea_bags += int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col] = "*"
        if tea_bags >= 10:
            print("She did it! She went to the party.")
            break
    else:
        matrix[alice_row][alice_col] = "*"

for row in matrix:
    print(" ".join(row))
