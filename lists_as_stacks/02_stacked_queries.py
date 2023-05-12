the_stack = []
result = []
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == '1':
        the_stack.append(int(command[1]))
    elif command[0] == '2' and the_stack:
        the_stack.pop()
    elif command[0] == '3' and the_stack:
        print(max(the_stack))
    elif command[0] == '4' and the_stack:
        print(min(the_stack))
for _ in range(len(the_stack)):
    result.append(the_stack.pop())
print(*result, sep=", ")
