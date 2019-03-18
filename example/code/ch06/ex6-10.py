# function
# function: return sum of two values
def sum(a, b):
    return a + b
    
# function: using function as parameter    
def operate_on(x, y, func):
    return func(x, y)

r = operate_on(16, 20, sum)   # call function
print("operate_on(16, 20, sum) = ", str(r))
          
r = operate_on(10, 40, lambda a,b: a+b)   # call function with anonymous function
print("operate_on(10, 40, anonymous_function) =", r)


