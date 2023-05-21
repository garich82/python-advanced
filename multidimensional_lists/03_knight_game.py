size = int(input())
matrix = [list(input()) for _ in range(size)]
positions = (
    (-2, -1),  # Up Left
    (-2, 1),   # Up Right
    (-1, 2),   # Right Up
    (1, 2),    # Right Down
    (2, 1),    # Down Right
    (2, -1),   # Down Left
    (1, -2),   # Left Down
    (-1, -2)   # Left Up
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_most_attacks_pos = [row, col]
                    max_attacks = attacks

    if knight_with_most_attacks_pos:
        matrix[knight_with_most_attacks_pos[0]][knight_with_most_attacks_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)