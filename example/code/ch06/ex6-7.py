# function
# global variables
a = 1
b = 2
# funcA
def funcA():
    c = 3  # local variable    
    print("In funcA : a =", a)
    print("In funcA : b =", b)
    print("In funcA : c =", c)
    
# funcB
def funcB():
    a = 3  # local variable
    print("In funcB : a =", a)
    print("In funcB : b =", b)
    # print("funcB : c =", c)

print("global variable a =", a)
print("global variable b =", b)

funcA()  # call funcA
print("After calling funcA : a =", a)
print("After calling funcA : b =", b)

funcB()  # call funcB
print("After calling funcB : a =", a)
print("After calling funcB : b =", b)
          




