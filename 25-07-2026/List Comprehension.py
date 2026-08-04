marks=[40,50,60,70]

#Without comprehension
new_marks=[]

for mark in marks:
    new_marks.append(mark+5)

print(new_marks)

#With comprehension
new_marks=[mark+5 for mark in marks]
print(new_marks)