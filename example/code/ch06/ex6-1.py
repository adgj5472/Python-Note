# function
# function: show message
def print_msg():
    print("Welcome to Python programming!")

# function: sum of 1..10 
def sum_to_ten():
    s = 0   
    for i in range(1, 11): # for loop
        s += i
    print("sum of 1..10 =", s)

print_msg()   # call function
sum_to_ten()
