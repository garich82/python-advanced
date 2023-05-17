from collections import deque

chocolates = [int(n) for n in input().split(", ")]
cups = deque([int(n) for n in input().split(", ")])
milkshakes = 0

while milkshakes < 5 and chocolates and cups:
    choc = chocolates.pop()
    while choc < 0 and chocolates:
        choc = chocolates.pop()
    cup = cups.popleft()
    while cup < 0 and cups:
        cup = cups.popleft()

    if cup == choc and cup > 0:
        milkshakes += 1
    else:
        if choc > 0:
            chocolates.append(choc - 5)
        if cup > 0:
            cups.append(cup)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print("Chocolate:", end=" ")
    print(*chocolates, sep=", ")
else:
    print("Chocolate: empty")

if cups:
    print("Milk:", end=" ")
    print(*cups, sep=", ")
else:
    print("Milk: empty")
