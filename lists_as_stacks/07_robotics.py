from datetime import datetime, timedelta
from collections import deque

robots = {}
products = deque()

for r in input().split(";"):
    name, time_needed = r.split('-')
    robots[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")

adding_product = input()
while adding_product != "End":
    products.append(adding_product)
    adding_product = input()

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()
    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1
        if robots[name][1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
    else:
        name, value = free_robots[0]
        robots[name][1] = robots[name][0]
        print(f"{name} - {product} [{factory_time:%H:%M:%S}]")
