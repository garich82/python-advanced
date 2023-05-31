numbers_dictionary = {}

line = input("Type the number as a word: ")

while line != "Search":
    number_as_string = line
    try:
        number = int(input("Type the number with digits: "))
    except ValueError:
        print("The variable number must be an integer")
    numbers_dictionary[number_as_string] = number
    line = input("Type the number as a word or 'Search' to move on: ")

line = input("Type the number you wish to search as a word: ")

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number doesn't exist in the dictionary!")
    line = input("Type the number you wish to search or 'Remove' to continue: ")

line = input("Type the number you wish to delete: ")

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary!")
    line = input("Type the number you wish to delete or 'End' to terminate: ")


print("\nFinal state of the dictionary:")
print(numbers_dictionary)

