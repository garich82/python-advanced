N = int(input())
odd_set = set()
even_set = set()

for i in range(1, N+1):
    values = sum([ord(letter) for letter in input()]) // i
    if values % 2 == 0:
        even_set.add(values)
    else:
        odd_set.add(values)

first_set_sum = sum(odd_set)
second_set_sum = sum(even_set)

if first_set_sum == second_set_sum:
    print(*odd_set.union(even_set), sep=", ")
elif first_set_sum > second_set_sum:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")