import os

file_name = "numbers.txt"
path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, file_name)

try:
    file = open(file_path, 'r')
    content_lines = file.read().split("\n")
    numbers = [int(el) for el in content_lines if el]
    print(sum(numbers))
except FileNotFoundError:
    print("File not found")


