# function
# function: no return value
def print_age(age):
    if age <= 18:
        print("Too young!")        
        return  # exit function
    print("Age =", age)            

# function: return boolean
def is_valid_num(no):
    if no >= 0 and no <= 200.0:
        return True  # legal
    else:
        return False # illegal

# function: return value
def convert_to_f(c):
    f = (9.0 * c) / 5.0 + 32.0
    return f

c = 100.00
print_age(15)  # call function
print_age(22)

# function returning data
if is_valid_num(c):
    print("legal!")
else:
    print("illegal")

f = convert_to_f(c)
print("Celsius " + str(c) + " = Fahrenheit" + str(f))


