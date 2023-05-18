rows, columns = [int(x) for x in input().split()]
matrix = [[el for el in input().split()] for _ in range(rows)]
counter = 0

for i in range(rows - 1):
    for j in range(columns - 1):
        el_1 = matrix[i][j]
        el_2 = matrix[i+1][j]
        el_3 = matrix[i][j+1]
        el_4 = matrix[i+1][j+1]
        if el_1 == el_2 == el_3 == el_4:
            counter += 1

print(counter)

