import os
import re


def read_content(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File does not exist, program is ending...")
        exit(0)


root_dir = os.path.dirname(os.path.abspath(__file__))
words_file_name = "words.txt"
words_file_path = os.path.join(root_dir, words_file_name)
text_file_name = "text.txt"
text_file_path = os.path.join(root_dir, text_file_name)

words = read_content(words_file_path).lower().split()
text_content = re.findall(r'\w+', read_content(text_file_path).lower())

words_count = {}
for word in text_content:
    if word in words:
        if word not in words_count:
            words_count[word] = 0
        words_count[word] += 1

sorted_words_count = sorted(words_count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words_count:
    print(f"{word} - {count}")
