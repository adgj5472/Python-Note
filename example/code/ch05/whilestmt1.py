# while stmt
m = int(input("Input factorial => "))
r = 1
n = 1
while n <= m:
    r = r * n
    n = n + 1
print(str(m) + "! =", r)
