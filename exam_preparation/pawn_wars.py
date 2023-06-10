matrix = [input().split() for _ in range(8)]

columns_mapper = {i: chr(ord('a') + i) for i in range(8)}
rows_mapper = {i: 8 - i for i in range(8)}

winner = None
winning_column = None
winning_row = None

b_positions = ((row_num, col_num) for row_num, row in enumerate(matrix)
               for col_num, element in enumerate(row) if element == 'b')
w_positions = ((row_num, col_num) for row_num, row in enumerate(matrix)
               for col_num, element in enumerate(row) if element == 'w')

black_row, black_column = next(b_positions)
white_row, white_column = next(w_positions)

if abs(black_column - white_column) == 1:  # Case where pawns are sitting on neighbouring columns:

    if (black_row - white_row) % 2 != 0:  # Case where white pawn will capture:
        winner = "White"
        winning_column = columns_mapper[black_column]
        winning_row = rows_mapper[black_row + (white_row - black_row) // 2]
    else:
        winner = "Black"
        winning_column = columns_mapper[white_column]
        winning_row = rows_mapper[(white_row + black_row) / 2]

    print(f"Game over! {winner} win, capture on {winning_column}{winning_row}.")

else:  # Case where pawns are NOT sitting on neighbouring columns

    if white_row <= (7 - black_row):  # Case where white pawn will be promoted first
        winner = "White"
        winning_column = columns_mapper[white_column]
        winning_row = 8
    else:
        winner = "Black"
        winning_column = columns_mapper[black_column]
        winning_row = 1

    print(f"Game over! {winner} pawn is promoted to a queen at {winning_column}{winning_row}.")
