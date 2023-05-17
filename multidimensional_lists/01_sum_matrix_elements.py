rows, columns = map(int, input().split(", "))

matrix = []

for i in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    matrix.append(inner_list)

sum_nums = 0

for row_index in range(rows):
    for col_index in range(columns):
        sum_nums += matrix[row_index][col_index]

print(sum_nums)
print(matrix)