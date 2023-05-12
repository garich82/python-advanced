from collections import deque

kids = deque(input().split())
toss = int(input())

while len(kids) > 1:
    for _ in range(toss - 1):
        current_kid = kids.popleft()
        kids.append(current_kid)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids[0]}")


