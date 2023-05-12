from collections import deque

text = input()
stack = deque([x for x in text])
open_parentheses = []

while stack:
    current = stack.popleft()
    if current in "([{":
        open_parentheses.append(current)
    elif len(open_parentheses) == 0:
        print("NO")
        break
    elif open_parentheses.pop() + current not in "()[]{}":
        print("NO")
        break
else:
    print("YES")
