# set
# create
s1 = {1, 2, 3}
s2 = {1, 'Hello', 3.5}
s3 = set()
s4 = set(["tom", "mary", "joe"])
s5 = set("Python")

# print items
print(s1)
print("s2 = " + str(s2))
print("s3 = " + str(s3))
print("s4 = " + str(s4))
print("s5 = " + str(s5))

# visit items
for e in s1:
    print(e, end=" ")
