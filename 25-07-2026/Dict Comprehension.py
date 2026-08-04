students = ["Ram", "Shyam", "Sita", "Gita", "Hari"]

#Without comprehension
attendance = {}

for student in students:
    attendance[student] = 12

print(attendance)

#with comprehension

attendance = {student:12 for student in students}

print(attendance)