def words_sorting(*args):
    word_dictionary = {}
    for word in args:
        word_value = 0
        for char in word:
            word_value += ord(char)
        word_dictionary[word] = word_value

    total_sum = sum(value for value in word_dictionary.values())

    if total_sum % 2 == 0:
        word_dictionary = dict(sorted(word_dictionary.items()))
    else:
        word_dictionary = dict(sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True))

    ready_to_print = ''
    for key, value in word_dictionary.items():
        ready_to_print += f'{key} - {value}\n'

    return ready_to_print


print(words_sorting('escape','charm','mythology'))

print(
 words_sorting(
 'escape',
 'charm',
 'eye'
 ))


print(
 words_sorting(
 'cacophony',
 'accolade'
 ))
