#Dictionary Comprehension

n = int(input("Enter a number: "))
table_dict = {
    i: [i*j for j in range(1, n+1)]
    for i in range(1, n+1)
}

print(table_dict)