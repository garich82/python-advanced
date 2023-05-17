from collections import deque

numbers = deque([int(num) for num in input().split()])
target = int(input())

while len(numbers) > 1:
    first_num = numbers.popleft()
    for i in range(len(numbers)):
        if first_num + numbers[i] == target:
            print(f"{first_num} + {numbers[i]} = {target}")
            numbers.remove(numbers[i])
            break
