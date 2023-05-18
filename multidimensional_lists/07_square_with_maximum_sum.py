rows, cols = [int(el) for el in input().split(", ")]
matrix = []

for _ in range(rows):
    current_row = [int(el) for el in input().split(", ")]
    matrix.append(current_row)

submatrix = []
max_sum = 0

for row_index in range(rows-1):
    for col_index in range(cols-1):
        current_element = matrix[row_index][col_index]
        element_below = matrix[row_index+1][col_index]
        element_beside = matrix[row_index][col_index+1]
        element_diagonal = matrix[row_index+1][col_index+1]
        current_sum = current_element + element_below + element_beside + element_diagonal
        if current_sum > max_sum:
            max_sum = current_sum
            submatrix = [[current_element, element_beside], [element_below, element_diagonal]]

for i in range(2):
    print(submatrix[i][0], submatrix[i][1])
print(max_sum)

