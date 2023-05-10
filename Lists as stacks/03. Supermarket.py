import time
from collections import deque

for i in range(10):
    list_queue = [element for element in range(1, 100000)]
    queue = deque(list_queue)

    start_time = time.time()

    while list_queue:
        list_queue.pop(0)

    end_time = time.time() - start_time

    print(f"as list: {end_time}")

    start_time = time.time()

    while queue:
        queue.popleft()

    end_time_2 = time.time() - start_time
    print(f"as queue: {end_time_2}")

    print(f"Queue is {end_time // end_time_2} times faster")




