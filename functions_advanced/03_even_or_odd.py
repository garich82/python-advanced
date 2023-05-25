def even_odd(*args):
    command = args[len(args) - 1]
    numbers = []
    for n in range(len(args) - 1):
        numbers.append(args[n])
    if command == "even":
        return [n for n in numbers if n % 2 == 0]
    else:
        return [n for n in numbers if n % 2 != 0]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))