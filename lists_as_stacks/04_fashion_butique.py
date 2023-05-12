clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
racks_count = 1
current_rack = rack_capacity

while clothes:
    cloth = clothes.pop()
    if current_rack < cloth:
        racks_count += 1
        current_rack = rack_capacity
    current_rack -= cloth

print(racks_count)
