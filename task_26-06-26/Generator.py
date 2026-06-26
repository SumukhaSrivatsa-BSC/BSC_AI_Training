#Generator is something thatproduces values one at a time, only when neede
# memory-efficient iteration,remember the state of the function(where it left earlier), pause and resume

def my_gen():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")
    yield 3

g = my_gen()
print(next(g))
print(next(g))
print(next(g))


# function ≠ executed completely
# function = pause + resume + continue

n = int(input("Enter a number: "))
for i in range(1, n+1):
    row = (i*j for j in range(1, n+1))#generate → give → forget → generate → give → forget
    for val in row:  
        print(val, end=" ")
    print()