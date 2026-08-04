numbers=[1, 2, 3, 4, 5]

#without comprehension

square_dict={}

for n in numbers:
    square_dict[n] = n**2

print(square_dict)

#with comprehension

square_dict={n:n**2 for n in numbers}

print(square_dict)