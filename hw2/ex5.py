
records = []
db = {}

text = input("Введите Предмет_Фамилия_Оценка\n")
while True:
    if(len(text) == 0):
        break
    else:
        records.append(tuple(text.split(" ")))
    text = input()

for subject, student, grade in records:
    if subject in db:
        if student in db[subject]:
            db[subject][student] = f"{db[subject][student]} {grade}"
        else:
            db[subject][student] = grade
    else:
        db[subject] = {student: grade}

for key in db:
    print(key)
    for student, grades in db[key].items():
        print(f"{student} {grades}")
    print()