from collections import deque

green_light = int(input())
free_window = int(input())
command = input()
cars = deque()
counter_cars = 0

while command != "END":
    if command == "green" and cars:
        timer = green_light
        while timer > 0 and cars:
            passing_car = cars.popleft()
            timer -= len(passing_car)
            counter_cars += 1
        if timer < 0:
            timer += free_window
            if timer < 0:
                hit_at = passing_car[len(passing_car) + timer]
                print(f"A crash happened!\n{passing_car} was hit at {hit_at}.")
                break
    else:
        cars.append(command)
    command = input()
else:
    print(f"Everyone is safe.\n{counter_cars} total cars passed the crossroads.")
