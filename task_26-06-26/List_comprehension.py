#List comprehension is a short way to create lists using loops
n = int(input("Enter a number: "))
table = [[i*j for j in range(1, n+1)] for i in range(1, n+1)]

for row in table:
    print(row)

    
    # print(*row)   o/t- 1 2 3 4 5 without brackets because * is used to unpack the list and print the values without brackets like print(1,2,3,4,5) instead of print([1,2,3,4,5])-->print(1,2,3,4,5)