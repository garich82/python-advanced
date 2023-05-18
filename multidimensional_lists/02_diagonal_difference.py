size = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(size)]

primary_diagonal = []
for i in range(size):
    primary_diagonal.append(matrix[i][i])

secondary_diagonal = []
for i in range(size):
    secondary_diagonal.append(matrix[i][size - 1 - i])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))