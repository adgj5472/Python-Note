# dictionary
d1 = {1:1, 2:4, "name":"tom", "age":20, 5:22}
print("d1 = " + str(d1))

# use del keyword
del d1[2]
print("del d1[2] = " + str(d1))
del d1["age"]
print("del d1['age'] = " + str(d1))

# pop(): remove/return specific item
e1 = d1.pop(5)
print("e1 = d1.pop(5) = " + str(d1))
print("e1 = " + str(e1))

# popitem(): remove/return any item
e2 = d1.popitem()
print("e2 = d1.popitem() = " + str(d1))
print("e2 = " + str(e2))

# clear(): remove all items
d1.clear()
print("d1 = " + str(d1))
