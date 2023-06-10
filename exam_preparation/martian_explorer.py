from collections import deque

SIZE = 6
field = [input().split() for _ in range(SIZE)]
rover_position = next((row_num, col_num) for row_num, row in enumerate(field) for
                  col_num, element in enumerate(row) if element == 'E')
water_deposits = next(((row_num, col_num) for row_num, row in enumerate(field) for
                  col_num, element in enumerate(row) if element == 'W'), None)
metal_deposits = next(((row_num, col_num) for row_num, row in enumerate(field) for
                  col_num, element in enumerate(row) if element == 'M'), None)
concrete_deposits = next(((row_num, col_num) for row_num, row in enumerate(field) for
                     col_num, element in enumerate(row) if element == 'C'), None)
rock_positions = next(((row_num, col_num) for row_num, row in enumerate(field) for
                  col_num, element in enumerate(row) if element == 'R'), None)

commands = deque(input().split(", "))

directions_mapper = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

water_found = metal_found = concrete_found = 0


def update_rover_position(position, movement):
    rover_row, rover_column = position
    row_change, column_change = movement
    new_row = rover_row + row_change
    new_column = rover_column + column_change
    if new_row < 0:
        new_row = SIZE - 1
    elif new_row >= SIZE:
        new_row = 0
    elif new_column < 0:
        new_column = SIZE - 1
    elif new_column >= SIZE:
        new_column = 0

    return new_row, new_column


while commands:
    direction = commands.popleft()
    rover_position = update_rover_position(rover_position, directions_mapper[direction])
    row, col = rover_position

    if field[row][col] == "R":
        print(f"Rover got broken at {rover_position}")
        break
    elif field[row][col] == "W":
        print(f"Water deposit found at {rover_position}")
        water_found += 1
    elif field[row][col] == "M":
        print(f"Metal deposit found at {rover_position}")
        metal_found += 1
    elif field[row][col] == "C":
        print(f"Concrete deposit found at {rover_position}")
        concrete_found += 1

if all([water_found > 0, metal_found > 0, concrete_found > 0]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")