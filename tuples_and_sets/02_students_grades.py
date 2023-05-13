from statistics import mean

count = int(input())

student_grades = {}

for _ in range(count):
    name, grade = input().split()
    grade = float(grade)

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for name, grades in student_grades.items():
    avg = 0
    count = 0
    suma = 0
    for grade in grades:
        suma += grade
        count += 1
    avg = suma / count
    print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grades])} (avg: {avg:.2f})")
