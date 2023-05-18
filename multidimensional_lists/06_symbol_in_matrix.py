# rowcol = int(input())
#
# matrix = []
# for i in range(rowcol):
#     current_row = list(input())
#     matrix.append(current_row)
#
# search_for = input()
#
# found = False
#
# for i in range(rowcol):
#     if found:
#         break
#     for j in range(rowcol):
#         if matrix[i][j] == search_for:
#             print(f"({i}, {j})")
#             found = True
#             break
#
# if not found:
#     print(f"{search_for} does not occur in the matrix")

def find_element_in_matrix(matrix, element):
    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == searched_symbol:
                return (row_index, col_index)


n = int(input())

matrix = []

for i in range(n):
    current_row = list(input())
    matrix.append(current_row)

searched_symbol = input()

position = find_element_in_matrix(matrix, searched_symbol)

if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")