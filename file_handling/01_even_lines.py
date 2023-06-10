# This script reads a text file, processes its lines,
# and prints the reversed words of every 2nd line.
# The text file is specified by the 'file_path' variable.
# Lines are processed by replacing some characters (-,.!?)
# with '@', reversing the words, and printing the result.
# If the file does not exist, a FileNotFoundError is caught
# and an appropriate message is printed.


file_path = "files/text_file.txt"

try:
    with open(file_path, "r") as file:
        lines_content = file.readlines()

        for index, line in enumerate(lines_content):
            if index % 2 == 0:
                line = line.replace("-", "@").replace(",", "@").replace(".", "@"). \
                    replace("!", "@").replace("?", "@")
                line = line.rstrip('\n')
                words = line.split()
                reversed_words = ' '.join(reversed(words))

                print(reversed_words)


except FileNotFoundError:
    print(f"Such file {file_path} does not exists!")
