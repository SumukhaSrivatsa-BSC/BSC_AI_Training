students = [["Ram", "Riya"], ["John", "Sara"], ["Tom", "David"]]

# Without comprehension

all_students = []
for student in students:
    for name in student:
        all_students.append(name)

print(all_students)

# with comprehension

all_students = [name for student in students for name in student]

print(all_students)
