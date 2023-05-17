from collections import deque

boxes = deque(int(i) for i in input().split())
magic_values = deque(int(i) for i in input().split())
crafted_items = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}
presents_ready = False

while boxes and magic_values:
    box = boxes.pop()
    magic = magic_values.popleft()

    total_magic_level = box * magic

    if total_magic_level == 150:
        crafted_items["Doll"] += 1
    elif total_magic_level == 250:
        crafted_items["Wooden train"] += 1
    elif total_magic_level == 300:
        crafted_items["Teddy bear"] += 1
    elif total_magic_level == 400:
        crafted_items["Bicycle"] += 1

    if total_magic_level < 0:
        boxes.append(box + magic)
    elif total_magic_level > 0 and total_magic_level not in (150, 250, 300, 400):
        boxes.append(box+15)
    elif box == 0 and magic != 0:
        magic_values.appendleft(magic)
    elif magic == 0 and box != 0:
        boxes.append(box)
    elif magic == 0 and box == 0:
        pass

if ((crafted_items["Doll"] > 0 and crafted_items["Wooden train"] > 0) or
        (crafted_items["Teddy bear"] > 0 and crafted_items["Bicycle"] > 0)):
    presents_ready = True

if presents_ready:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    print("Materials left:", end=" ")
    print(*sorted(boxes, reverse=True), sep=", ")

if magic_values:
    print("Magic left:", end=" ")
    print(*magic_values, sep=", ")

for item, count in sorted(crafted_items.items()):
    if count > 0:
        print(f"{item}: {count}")

