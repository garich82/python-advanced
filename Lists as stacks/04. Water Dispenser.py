from collections import deque

water = int(input())
people = deque()

name = input()
while name != "Start":
    people.append(name)
    name = input()

command = input()
while command != "End":
    try:
        required = int(command)
        if required <= water:
            print(f"{people.popleft()} got water")
            water -= required
        else:
            print(f"{people.popleft()} must wait")
    except ValueError:
        refill = command.split()
        water += int(refill[1])
    command = input()

print(f"{water} liters left")
