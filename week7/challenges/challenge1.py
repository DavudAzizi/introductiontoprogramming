students = []

while True:
    name = input("Name: ")

    if name == "":
        break

    marks = []

    for i in range(3):
        mark = float(input(f"Mark {i + 1}: "))
        marks.append(mark)

    average = sum(marks) / len(marks)

    students.append({
        "name": name,
        "average": average
    })

print("\nResults:")

for student in students:
    print(f"{student['name']}: {student['average']:.2f}")
