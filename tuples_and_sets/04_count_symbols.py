text = input()
unique_letters = {}

for i in range(len(text)):
    if text[i] not in unique_letters:
        unique_letters[text[i]] = 0
    unique_letters[text[i]] += 1

for key, value in sorted(unique_letters.items()):
    print(f"{key}: {value} time/s")


# occurrences = {}
#
# for letter in input():
#     occurrences[letter] = occurrences.get(letter, 0) + 1
