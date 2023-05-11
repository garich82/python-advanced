numbers = list(map(int, input().split()))
for _ in range(len(numbers)):
    print(numbers.pop(), end=' ')
