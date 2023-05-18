rows = int(input())
matrix = []

for _ in range(rows):
    current_row = [int(el) for el in input().split()]
    matrix.append(current_row)

sum_diagonal = 0
for i in range(rows):
    sum_diagonal += matrix[i][i]

print(sum_diagonal)
