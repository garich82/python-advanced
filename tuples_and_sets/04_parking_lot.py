cars = set()

for _ in range(int(input())):
    direction, car = input().split(', ')
    if direction == "IN":
        cars.add(car)
    else:
        cars.remove(car)

print('\n'.join(cars)) if cars else print("Parking Lot is Empty")