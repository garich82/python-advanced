from collections import deque

text = input()
stack = deque([x for x in text])
balanced = True

while stack:
    left_end = stack.popleft()
    right_end = stack.pop()
    if abs(ord(left_end) - ord(right_end)) > 2:
        print("NO")
        balanced = False
        break

if balanced:
    print("YES")