# exception
try:
    num = eval(input("Enter a number => "))
    print("value =", num)    
except NameError as e:
    print("Error: " + str(e))

    