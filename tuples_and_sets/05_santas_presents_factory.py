from collections import deque

boxes = deque([int(i) for i in input().split()])
magic_values = deque([int(i) for i in input().split()])
crafted_items = {}

while boxes and magic_values:
    box = boxes.pop()
    magic = magic_values.popleft()

    total_magic_level = box * magic

    if total_magic_level == 150:
        if "Doll" not in crafted_items:
            crafted_items["Doll"] = 0
        else:
            crafted_items["Doll"] += 1
    elif total_magic_level == 250:
        if "Wooden train" not in crafted_items:
            crafted_items["Wooden train"] = 0
        else:
            crafted_items["Wooden train"] += 1
    elif total_magic_level == 300:
        if "Teddy bear" not in crafted_items:
            crafted_items["Teddy bear"] = 0
        else:
            crafted_items["Teddy bear"] += 1
    elif total_magic_level == 400:
        if "Bicycle" not in crafted_items:
            crafted_items["Bicycle"] = 0
        else:
            crafted_items["Bicycle"] += 1
    elif total_magic_level < 0:
        box