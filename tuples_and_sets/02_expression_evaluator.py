from collections import deque

expression = input().split()
numbers = deque()
result = 0
-
for i in range(len(expression)):
    try:
        numbers.append(int(expression[i]))
    except ValueError:
        result = numbers.popleft()

        if expression[i] == '*':
            while numbers:
                result *= numbers.popleft()
        elif expression[i] == '+':
            while numbers:
                result += numbers.popleft()
        elif expression[i] == '-':
            while numbers:
                result -= numbers.popleft()
        elif expression[i] == '/':
            while numbers:
                result //= numbers.popleft()

        numbers.append(result)

print(result)
