from collections import deque

chocolates = [int(n) for n in input().split(", ")]
cups = deque([int(n) for n in input().split(", ")])
milkshakes = 0

while milkshakes < 5 and chocolates and cups:
    choc = chocolates.pop()
    cup = cups.popleft()

    if choc <= 0 and cup <= 0:
        pass
    elif choc <= 0:
        cups.appendleft(cup)
    elif cup <= 0:
        chocolates.append(choc)
    elif cup == choc:
        milkshakes += 1
    else:
        chocolates.append(choc - 5)
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
