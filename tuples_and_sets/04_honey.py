from collections import deque

bees = deque([int(i) for i in input().split()])
nectars = [int(i) for i in input().split()]
operators = deque(input().split())
honey = 0

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar < bee:
        bees.appendleft(bee)
    else:
        operator = operators.popleft()
        produce = 0
    
        if operator == "+":
            produce = bee + nectar
        elif operator == "-":
            produce = abs(bee - nectar)
        elif operator == "*":
            produce = bee * nectar
        elif operator == "/" and nectar != 0:
            produce = bee / nectar

        honey += produce

print(f"Total honey made: {honey}")
if bees:
    print("Bees left:", end=" ")
    print(*bees, sep=", ")
if nectars:
    print("Nectar left:", end=" ")
    print(*nectars, sep=", ")
