file_path = "files/text_file.txt"


def count_letters_punctuation(text):
    count_letter = 0
    count_punctuation = 0

    for char in text:
        if char.isalpha():
            count_letter += 1
        elif char in ('.', ',', '!', '?', '-', ';', ':'):
            count_punctuation += 1

    return count_letter, count_punctuation


try:
    with open(file_path, "r") as file:
        lines_content = file.readlines()

        for index in range(len(lines_content)):
            line = lines_content[index].rstrip('\n')

            letters_count, punctuation_count = count_letters_punctuation(line)

            print(f"Line {index+1}: {line} ({letters_count})({punctuation_count})")

except FileNotFoundError:
    print(f"Such file {file_path} does not exists!")
