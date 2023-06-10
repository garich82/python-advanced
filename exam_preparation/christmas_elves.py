from collections import deque


elves = deque([int(i) for i in input().split()])
boxes = deque([int(i) for i in input().split()])

toys_produced = 0
energy_spent = 0
work_counter = 0

while elves and boxes:
    current_elf = elves.popleft()
    current_box = boxes.pop()

    if current_elf < 5:
        boxes.append(current_box)
        continue

    work_counter += 1
    if work_counter % 3 == 0 and current_elf >= current_box * 2:
        current_elf -= current_box * 2
        energy_spent += current_box * 2
        if work_counter % 5 != 0:
            toys_produced += 2
            current_elf += 1
    elif work_counter % 5 == 0 and current_elf >= current_box:
        current_elf -= current_box
        energy_spent += current_box
    elif current_elf >= current_box and work_counter % 3 != 0:
        toys_produced += 1
        current_elf = current_elf - current_box + 1
        energy_spent += current_box
    else:
        boxes.append(current_box)
        current_elf *= 2

    elves.append(current_elf)

print(f"Toys: {toys_produced}")
print(f"Energy: {energy_spent}")
if elves:
    print(f"Elves left: {', '.join(str(element) for element in elves)}")
if boxes:
    print(f"Boxes left: {', '.join(str(element) for element in boxes)}")
