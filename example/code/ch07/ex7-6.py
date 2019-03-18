# exception
try:
    n1, n2 = eval(input("Input two integers(n1,n2) => "))
    r = n1 / n2
    print("r =", r)    
except ZeroDivisionError:
    print("Error: Devided by zero!")
except SyntaxError:
    print("Error: Please separate input data by comma!")
except:
    print("Error: Input error!")    