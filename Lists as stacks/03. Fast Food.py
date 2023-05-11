from collections import deque

food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders:
    current_order = orders.popleft()

    if food >= current_order:
        food -= current_order
    else:
        orders.appendleft(current_order)
        print(f"Orders left: {' '.join(map(str, orders))}")
        break

if len(orders) == 0:
    print("Orders complete")

