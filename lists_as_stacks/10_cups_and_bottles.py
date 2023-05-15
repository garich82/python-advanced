from collections import deque

cups = deque([int(elem) for elem in input().split()])
bottles = [int(elem) for elem in input().split()]
waste = 0

while cups and bottles:
    curr_cup = cups.popleft()
    while curr_cup > 0 and bottles:
        curr_bottle = bottles.pop()
        if curr_cup >= curr_bottle:
            curr_cup -= curr_bottle
        else:
            curr_cup -= curr_bottle
            waste += - curr_cup

if bottles:
    print("Bottles:", *bottles, sep=' ')
else:
    print("Cups:", *cups, sep=' ')
print(f"Wasted litters of water: {waste}")
