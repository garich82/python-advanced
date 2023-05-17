set_a = {int(i) for i in input().split()}
set_b = {int(i) for i in input().split()}
n = int(input())

for _ in range(n):
    command = input()

    if command == "Check Subset":
        print(set_a.issubset(set_b) or set_b.issubset(set_a))

    else:
        commands = command.split()
        numbers = [int(commands[i]) for i in range(2,len(commands))]

        if commands[0] == "Add" and commands[1] == "First":
            for i in range(len(numbers)):
                set_a.add(numbers[i])
        elif commands[0] == "Add" and commands[1] == "Second":
            for i in range(len(numbers)):
                set_b.add(numbers[i])
        elif commands[0] == "Remove" and commands[1] == "First":
            for i in range(len(numbers)):
                set_a.discard(numbers[i])
        else:
            for i in range(len(numbers)):
                set_b.discard(numbers[i])

print(*sorted(set_a), sep=", ")
print(*sorted(set_b), sep=", ")
