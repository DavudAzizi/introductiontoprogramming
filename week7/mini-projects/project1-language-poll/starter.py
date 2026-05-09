students = []

while True:
    name = input("Name: ")

    if name == "":
        break

    age = int(input("Age: "))
    grade = input("Grade: ")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)

print("\nStudent List:")
for student in students:
    print(f"{student['name']} - Age: {student['age']} - Grade: {student['grade']}")
