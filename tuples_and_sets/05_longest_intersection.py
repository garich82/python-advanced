# longest_intersection = list()
#
# for _ in range(int(input())):
#     text = input().split("-")
#     first = text[0].split(",")
#     second = text[1].split(",")
#     first_start = int(first[0])
#     first_end = int(first[1])
#     second_start = int(second[0])
#     second_end = int(second[1])
#     set_a = set(range(first_start, first_end+1))
#     set_b = set(range(second_start, second_end+1))
#     intersection_length = len(set_a.intersection(set_b))
#     if intersection_length > len(longest_intersection):
#         longest_intersection = list(set_a.intersection(set_b))
#
# print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")

longest = list()

for _ in range (int(input())):
    first_data, second_data = [el.split(",") for el in input().split("-")]

    first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))

    intersection = first_range & second_range
    if len(intersection) > len(longest):
        longest = list(intersection)

print(f"Longest intersection is {longest} with length {len(longest)}")


