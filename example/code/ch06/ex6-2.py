# function
# function: sum of start..stop
def sum_to_n(start, stop):
    s = 0
    for i in range(start, stop+1):
        s += i
    print("Sum of " + str(start) + ".." + str(stop) + " = " + str(s))

m = 5
sum_to_n(1, 5)  # call function
sum_to_n(2, m + 2)

