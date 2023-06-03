try:
    file = open("text.txt")
    print(file.read())
except FileNotFoundError:
    print("File not found")