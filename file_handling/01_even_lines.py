file_path = "files/text_file.txt"

try:
    with open(file_path, "r") as file:
        lines_content = file.readlines()

        for index in range(len(lines_content)):

            if index % 2 == 0:
                line = lines_content[index]
                line = line.replace("-", "@").replace(",", "@").replace(".", "@"). \
                    replace("!", "@").replace("?", "@")
                line = line.rstrip('\n')
                words = line.split()
                reversed_words = ' '.join(reversed(words))

                print(reversed_words)


except FileNotFoundError:
    print(f"Such file {file_path} does not exists!")
