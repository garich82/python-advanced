def fill_the_box(height, length, width, *args):
    from collections import deque

    box_size = height * length * width
    finish = args.index("Finish")
    boxes = deque([box for box in args[:finish]])
    while boxes:
        box_size -= boxes.popleft()

        if box_size <= 0:
            boxes.append(abs(box_size))
            return f"No more free space! You have {sum(boxes)} more cubes."

    return f"There is free space in the box. You could put {box_size} more cubes."


print(
    fill_the_box(
        2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"
    ))
print(fill_the_box(5, 5,
2, 40, 11, 7, 3, 1, 5,
"Finish"))
print(fill_the_box(10, 10,
10, 40, "Finish", 2, 15,
30))
