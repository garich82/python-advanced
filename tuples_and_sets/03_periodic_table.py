elements = set()

for _ in range(int(input())):
    current_elements = input().split()
    for i in range (len(current_elements)):
        elements.add(current_elements[i])

print(*elements, sep="\n")