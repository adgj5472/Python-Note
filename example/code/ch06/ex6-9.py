# function
# function: return sum of two values
def sum(a, b):
    return a + b
    
# create anonymous function
square = lambda x: x * x

# assign function to reference
total = sum
r = square(10)   # call anonymous function
print("square(10) =", r)

r = sum(10, 5)   # call function
print("sum(10, 5) =", r)

r = total(10, 5) # call function using reference
print("total(10, 5) =", r)
          




