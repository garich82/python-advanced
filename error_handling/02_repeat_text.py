text = input()
times = input()
try:
    times = int(times)
    print(text * times)
except ValueError:
    print("Variable times must be an integer")