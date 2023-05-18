rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    current_row = [int(el) for el in input().split()]
    matrix.append(current_row)

for j in range(cols):
    current_col_sum = 0
    for i in range(rows):
        current_col_sum += matrix[i][j]
    print(current_col_sum)
