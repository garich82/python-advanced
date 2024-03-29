# This script provides basic file manipulation operations: Create, Add, Replace, and Delete.
# Users can interact with the script by entering commands in specified format.
# The script performs the corresponding file operation based on the entered command and parameters.
# The program continues to accept user commands until the "End" command is entered.


import os


def create_file(file_name):
    file_path = f"files/{file_name}"
    file = open(file_path, 'w')
    file.close()


def add_to_file(file_name, content):
    file_path = f"files/{file_name}"
    content_with_new_line = content + "\n"
    with open(file_path, 'a') as file:
        file.write(content_with_new_line)


def replace_in_file(file_name, old_string, new_string):
    file_path = f"files/{file_name}"

    try:
        with open(file_path, 'r') as file:
            content = file.read()

        updated_content = content.replace(old_string, new_string)

        with open(file_path, 'w') as file:
            file.write(updated_content)

    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    file_path = f"files/{file_name}"

    try:
        os.remove(file_path)

    except FileNotFoundError:
        print("An error occurred")


# Main program starts here

print("The input is in the following format: Command-filename-parameter_1-parameter_2")
print("Available commands are Create, Add, Replace or Delete")
print("Command 'Add' takes 1 parameter - content to be added")
print("Command 'Replace' takes 2 parameters - text to be replaced and substitution")
command_input = input("Type command: ")

while command_input != "End":
    commands = command_input.split('-')

    if commands[0] == "Create":
        create_file(commands[1])

    elif commands[0] == "Add":
        add_to_file(commands[1], commands[2])

    elif commands[0] == "Replace":
        replace_in_file(commands[1], commands[2], commands[3])

    elif commands[0] == "Delete":
        delete_file(commands[1])

    else:
        print("Invalid command")

    command_input = input("Type command or 'End' to terminate: ")