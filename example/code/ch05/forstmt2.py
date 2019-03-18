# for stmt
m = int(input("Input a value =>"))
s = 0
for i in range(m, 0, -1):
    print("i = ", str(i))
    s += i
print("sum = " + str(s))
