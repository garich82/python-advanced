size = int(input())
matrix = [[int(el) for el in input().split(", ")] for _ in range(size)]

primary_diagonal = []
for i in range(size):
    primary_diagonal.append(matrix[i][i])

secondary_diagonal = []
for i in range(size):
    secondary_diagonal.append(matrix[i][size - 1 - i])

print("Primary diagonal: ",end="")
print(*primary_diagonal, sep=", ", end=". ")
print(f"Sum: {sum(primary_diagonal)}")

print("Secondary diagonal: ",end="")
print(*secondary_diagonal, sep=", ", end=". ")
print(f"Sum: {sum(secondary_diagonal)}")