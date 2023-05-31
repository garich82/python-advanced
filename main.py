print("Enter/Paste your content. Type 'End' to finish.:")
text = []
line = input()
while line != "End":
    text.append(line)
    line = input()

new_text = ''.join(text)
print()
print()
print()
print()
mid = len(new_text) // 2
print(new_text[mid-10:mid+10])
