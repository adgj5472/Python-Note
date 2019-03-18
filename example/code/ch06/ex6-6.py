# function
# call function using keyword argument
def sum(a, b, c):
    return a + b + c

r1 = sum(1, 2, 3)       # positional(required) argument
r2 = sum(b=2, c=3, a=1) # keyword argument
r3 = sum(1, c=3, b=2)   # both of positional and keyword arguments
r4 = sum(1, 2, c=3)

print("sum =", r1)
print("sum =", r2)
print("sum =", r3)
print("sum =", r4)

