import random


def calculate_damage():
    hits = sum(random.choices([0, 1], weights=[1/3, 2/3]) for _ in range(18))
    return hits


def calculate_fight():
    fleet_a_size = int(input("Enter the size of Fleet A: "))
    fleet_b_size = int(input("Enter the size of Fleet B: "))

    fleet_a = [40 for _ in range(fleet_a_size)]
    fleet_b = [40 for _ in range(fleet_b_size)]

    while fleet_a and fleet_b:
        # Fleet A attacks Fleet B
        for _ in range(fleet_a_size):
            if fleet_b:
                damage = calculate_damage()
                ship_index = random.randint(0, len(fleet_b) - 1)
                fleet_b[ship_index] -= damage
                if fleet_b[ship_index] <= 0:
                    fleet_b.pop(ship_index)

        # Fleet B attacks Fleet A
        for _ in range(fleet_b_size):
            if fleet_a:
                damage = calculate_damage()
                ship_index = random.randint(0, len(fleet_a) - 1)
                fleet_a[ship_index] -= damage
                if fleet_a[ship_index] <= 0:
                    fleet_a.pop(ship_index)

    if fleet_a:
        winner = "Fleet A"
        winning_fleet = fleet_a
        losing_fleet = fleet_b
    else:
        winner = "Fleet B"
        winning_fleet = fleet_b
        losing_fleet = fleet_a

    print("Winner:", winner)
    print("Number of ships sunk by the winning fleet:", len(losing_fleet))
    print("Number of ships lost:", len(winning_fleet))
    print("Ships that survived:")

    for i, hit_points in enumerate(winning_fleet, start=1):
        print(f"Ship {i} - {hit_points}/40")


# Example usage:
calculate_fight()
