import random


class Ship:
    def __init__(self, ship_type, fleet_number):
        if ship_type == 'Carrack':
            self.ship_name = f'Carrack {fleet_number}'
            self.attack = 18
        elif ship_type == 'Cog':
            self.ship_name = f'Cog {fleet_number}'
            self.attack = 11
        else:
            raise ValueError("Invalid ship type")

        self.hit_points = 40

    def __str__(self):
        return f"{self.ship_name} - {self.hit_points} HP"


def calculate_damage(num_shots):
    total_damage = 0
    for _ in range(num_shots):
        if random.choices([0, 1], weights=[1/3, 2/3])[0] == 1:
            total_damage += 1
    return total_damage


def generate_fleet():
    fleet_a_carracks = int(input("Enter the number of Carracks in Fleet A: "))
    fleet_a_cogs = int(input("Enter the number of Cogs in Fleet A: "))
    fleet_b_carracks = int(input("Enter the number of Carracks in Fleet B: "))
    fleet_b_cogs = int(input("Enter the number of Cogs in Fleet B: "))

    fleet_a = [Ship('Carrack', i) for i in range(1, fleet_a_carracks + 1)] + [Ship('Cog', i) for i in range(1, fleet_a_cogs + 1)]
    fleet_b = [Ship('Carrack', i) for i in range(1, fleet_b_carracks + 1)] + [Ship('Cog', i) for i in range(1, fleet_b_cogs + 1)]

    return fleet_a, fleet_b


def print_fleet(fleet):
    for ship in fleet:
        print(ship)


def assign_damage(damage, fleet):
    num_ships = len(fleet)
    for _ in range(damage):
        if num_ships > 0:
            ship_index = random.randint(0, num_ships - 1)
            fleet[ship_index].hit_points -= 1
            if fleet[ship_index].hit_points <= 0:
                fleet.pop(ship_index)
                num_ships -= 1


def battle_round(fleet_a, fleet_b, round_num, fleet_a_initial_count, fleet_b_initial_count):
    print(f"--- Round {round_num} ---")

    # Calculate damage for Fleet A
    damage_a = sum([calculate_damage(ship.attack) for ship in fleet_a])

    # Calculate damage for Fleet B
    damage_b = sum([calculate_damage(ship.attack) for ship in fleet_b])

    # Assign damage to ships in Fleet B
    assign_damage(damage_a, fleet_b)

    # Assign damage to ships in Fleet A
    assign_damage(damage_b, fleet_a)

    # Calculate losses for each fleet
    fleet_a_losses = fleet_a_initial_count - len(fleet_a)
    fleet_b_losses = fleet_b_initial_count - len(fleet_b)

    # Print round summary
    print(f"Fleet A inflicted {damage_a} damage and lost {fleet_a_losses} ships.")
    print(f"Fleet B inflicted {damage_b} damage and lost {fleet_b_losses} ships.")

    # Print state of fleets
    print("\nFleet A:")
    print_fleet(fleet_a)

    print("\nFleet B:")
    print_fleet(fleet_b)

    print()


def simulate_battle():
    fleet_a, fleet_b = generate_fleet()
    fleet_a_initial_count = len(fleet_a)
    fleet_b_initial_count = len(fleet_b)
    round_num = 1

    while fleet_a and fleet_b:
        battle_round(fleet_a, fleet_b, round_num, fleet_a_initial_count, fleet_b_initial_count)
        round_num += 1

    print("--- Battle Summary ---")
    print(f"Total Rounds: {round_num - 1}")
    print(f"Fleet A ships remaining: {len(fleet_a)}")
    print(f"Fleet B ships remaining: {len(fleet_b)}")


# Start the battle simulation
simulate_battle()
