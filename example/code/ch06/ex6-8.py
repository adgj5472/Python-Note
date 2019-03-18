# function
# global variable
t = 1

# using global variable in function
def increment():
    # global t = 1
    global t  # using global variable t 
    t += 1
    print("In increment : t =", t)
    
# declare global variable in function
def global_var():
    # global x = 100
    global x
    x = 100
    print("In global_var : x =", x)

print("Global variable t =", (t)
increment()  # call increment
print("After calling increment : t =", t)
global_var()  # call global_var
print("After calling global_var : x =", x)
          




