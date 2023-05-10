text = input()

stack_parenthesis = []

for index in range(len(text)):
    if text[index] == '(':
        stack_parenthesis.append(index)
    elif text[index] == ')':
        pole_pos = stack_parenthesis.pop()
        last_pos = index + 1
        print(text[pole_pos:last_pos])
