from collections import deque


def remove_all(element, seq):
    while element in seq:
        seq.remove(element)


def remove_letter(letter, *words):
    for word in words:
        if letter in word:
            remove_all(letter, word)
    return words


rose = deque("rose")
tulip = deque("tulip")
daffodil = deque("daffodil")
lotus = deque("lotus")

vowels = deque(input().split())
consonants = deque(input().split())

while rose and tulip and daffodil and lotus and vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    rose, tulip, daffodil, lotus = remove_letter(current_vowel, rose, tulip, daffodil, lotus)
    rose, tulip, daffodil, lotus = remove_letter(current_consonant, rose, tulip, daffodil, lotus)

if not rose:
    print("Word found: rose")
elif not tulip:
    print("Word found: tulip")
elif not daffodil:
    print("Word found: daffodil")
elif not lotus:
    print("Word found: lotus")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
