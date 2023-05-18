row = int(input())
matrix = []

for _ in range(row):
    current_row = [int(el) for el in input().split(", ")]
    matrix.append(current_row)

flatten = []

for i in range(row):
    for j in range(len(matrix[i])):
        flatten.append(matrix[i][j])

print(flatten)