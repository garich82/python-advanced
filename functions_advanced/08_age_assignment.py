def age_assignment(*names, **values):
    result = []

    for key, value in values.items():
        for name in names:
            if key == name[0]:
                result.append(f"{name} is {value} years old.")

    return '\n'.join(sorted(result))


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))